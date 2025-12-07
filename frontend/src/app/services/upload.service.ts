import { Injectable } from '@angular/core';
import { HttpClient, HttpEventType } from '@angular/common/http';
import { Observable, Subject, from, of, concat } from 'rxjs';
import { map, switchMap, tap, mergeMap, concatMap, last, retry } from 'rxjs/operators';

export interface UploadProgress {
    status: 'progress' | 'complete' | 'error';
    percentage: number;
    dataset?: any;
    error?: any;
}

@Injectable({
    providedIn: 'root'
})
export class UploadService {
    private apiUrl = '/api/v1/datasets/upload';
    private CHUNK_SIZE = 5 * 1024 * 1024; // 5MB

    constructor(private http: HttpClient) { }

    uploadFile(file: File, name: string, format: string): Observable<UploadProgress> {
        const totalChunks = Math.ceil(file.size / this.CHUNK_SIZE);
        const progressSubject = new Subject<UploadProgress>();
        let uploadedChunks = 0;

        // 1. Initialize Upload
        this.http.post<{ upload_id: string, chunk_size: number }>(`${this.apiUrl}/init`, {
            filename: file.name,
            total_size: file.size,
            chunk_size: this.CHUNK_SIZE
        }).pipe(
            switchMap(initData => {
                const uploadId = initData.upload_id;
                const chunks = [];

                // Prepare serialization of chunks
                for (let i = 0; i < totalChunks; i++) {
                    const start = i * this.CHUNK_SIZE;
                    const end = Math.min(start + this.CHUNK_SIZE, file.size);
                    const chunkBlob = file.slice(start, end);
                    chunks.push({ index: i, blob: chunkBlob });
                }

                // 2. Upload Chunks (Sequential or limited parallel)
                // Using concatMap for sequential to be safe with server I/O, or mergeMap for parallel
                // User wanted Speed -> mergeMap with concurrency limit
                return from(chunks).pipe(
                    mergeMap(chunk => {
                        const formData = new FormData();
                        formData.append('upload_id', uploadId);
                        formData.append('chunk_index', chunk.index.toString());
                        formData.append('file', chunk.blob, `chunk_${chunk.index}`);

                        return this.http.post(`${this.apiUrl}/chunk`, formData).pipe(
                            retry(3), // Robustness
                            tap(() => {
                                uploadedChunks++;
                                const percentage = Math.round((uploadedChunks / totalChunks) * 100);
                                progressSubject.next({
                                    status: 'progress',
                                    percentage: percentage === 100 ? 99 : percentage // Hold at 99 until finalized
                                });
                            })
                        );
                    }, 3), // Concurrency: 3 parallel chunks
                    last(), // Wait for all to complete
                    // 3. Finalize
                    switchMap(() => {
                        return this.http.post(`${this.apiUrl}/finalize`, {
                            upload_id: uploadId,
                            name: name,
                            format: format
                        });
                    })
                );
            })
        ).subscribe({
            next: (dataset) => {
                progressSubject.next({
                    status: 'complete',
                    percentage: 100,
                    dataset: dataset
                });
                progressSubject.complete();
            },
            error: (err) => {
                progressSubject.next({
                    status: 'error',
                    percentage: 0,
                    error: err
                });
                progressSubject.error(err);
            }
        });

        return progressSubject.asObservable();
    }
}
