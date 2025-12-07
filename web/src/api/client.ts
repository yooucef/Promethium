import axios from 'axios';

const API_URL = 'http://localhost:8000/api/v1';

export const apiClient = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export interface Dataset {
    id: number;
    name: string;
    format: string;
    metadata_json: Record<string, any>;
    upload_time: string;
}

export interface Job {
    id: string;
    dataset_id: number;
    algorithm: string;
    status: 'QUEUED' | 'RUNNING' | 'COMPLETED' | 'FAILED';
    created_at: string;
    result_path?: string;
    error_message?: string;
}

export const fetchDatasets = async (): Promise<Dataset[]> => {
    const response = await apiClient.get<Dataset[]>('/datasets');
    return response.data;
};

export const fetchJobs = async (): Promise<Job[]> => {
    const response = await apiClient.get<Job[]>('/jobs');
    return response.data;
};

export const createJob = async (datasetId: number, algorithm: string, params: any) => {
    const response = await apiClient.post<Job>('/jobs', { dataset_id: datasetId, algorithm, params });
    return response.data;
};

export const uploadDataset = async (name: string, format: string, file: File) => {
    const formData = new FormData();
    formData.append('name', name);
    formData.append('format', format);
    formData.append('file', file);
    return apiClient.post<Dataset>('/datasets', formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
    });
};
