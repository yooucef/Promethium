import { Component, OnInit, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService, Dataset } from '../../services/api.service';
import { UploadService, UploadProgress } from '../../services/upload.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-dataset-browser',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './dataset-browser.html',
  styleUrls: ['./dataset-browser.css']
})
export class DatasetBrowserComponent implements OnInit {
  datasets = signal<Dataset[]>([]);
  selectedFile: File | null = null;
  datasetName = '';

  // Upload State
  uploading = false;
  progress = 0;
  uploadStatus = '';

  constructor(
    private api: ApiService,
    private uploadService: UploadService
  ) { }

  ngOnInit() {
    this.loadDatasets();
  }

  loadDatasets() {
    this.api.getDatasets().subscribe((data: Dataset[]) => this.datasets.set(data));
  }

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
    if (this.selectedFile && !this.datasetName) {
      // Auto-fill name
      this.datasetName = this.selectedFile.name.split('.')[0];
    }
  }

  upload() {
    if (!this.selectedFile || !this.datasetName) return;

    this.uploading = true;
    this.progress = 0;
    this.uploadStatus = 'Initializing...';

    // Assume SEGY for now as enforced by backend requirements
    const format = 'SEGY';

    this.uploadService.uploadFile(this.selectedFile, this.datasetName, format).subscribe({
      next: (event: UploadProgress) => {
        this.progress = event.percentage;

        if (event.status === 'progress') {
          this.uploadStatus = `Uploading... ${this.progress}%`;
        } else if (event.status === 'complete') {
          this.uploadStatus = 'Complete!';
          this.datasets.update(list => [...list, event.dataset]);
          setTimeout(() => {
            this.resetForm();
          }, 1500);
        }
      },
      error: (err) => {
        console.error('Upload failed', err);
        this.uploadStatus = 'Failed!';
        this.uploading = false; // Allow retry
      }
    });
  }

  resetForm() {
    this.uploading = false;
    this.selectedFile = null;
    this.datasetName = '';
    this.progress = 0;
    this.uploadStatus = '';
  }
}
