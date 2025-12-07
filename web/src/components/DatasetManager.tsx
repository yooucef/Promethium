import { useState, useEffect } from 'react';
import { fetchDatasets, uploadDataset, type Dataset } from '../api/client';
import { Upload, FileAudio } from 'lucide-react';

export const DatasetManager = () => {
    const [datasets, setDatasets] = useState<Dataset[]>([]);
    const [uploading, setUploading] = useState(false);

    useEffect(() => {
        loadDatasets();
    }, []);

    const loadDatasets = async () => {
        try {
            const data = await fetchDatasets();
            setDatasets(data);
        } catch (err) {
            console.error(err);
        }
    };

    const handleUpload = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        const formData = new FormData(e.currentTarget);
        const file = formData.get('file') as File;
        const name = formData.get('name') as string;
        const format = formData.get('format') as string;

        if (!file || !name) return;

        setUploading(true);
        try {
            await uploadDataset(name, format, file);
            await loadDatasets();
            (e.target as HTMLFormElement).reset();
        } catch (err) {
            alert('Upload failed');
        } finally {
            setUploading(false);
        }
    };

    return (
        <div className="card">
            <h2>Dataset Registry</h2>

            <form onSubmit={handleUpload} style={{ display: 'grid', gap: '1rem', marginBottom: '2rem' }}>
                <input name="name" placeholder="Dataset Name" className="input" required />
                <select name="format" className="input">
                    <option value="SEGY">SEG-Y</option>
                    <option value="SAC">SAC</option>
                    <option value="MINISEED">MiniSEED</option>
                </select>
                <input type="file" name="file" className="input" required />
                <button type="submit" className="btn" disabled={uploading}>
                    <Upload size={18} />
                    {uploading ? 'Uploading...' : 'Upload Dataset'}
                </button>
            </form>

            <div style={{ display: 'grid', gap: '0.5rem' }}>
                {datasets.map(ds => (
                    <div key={ds.id} style={{ display: 'flex', justifyContent: 'space-between', padding: '0.5rem', background: 'var(--bg-tertiary)', borderRadius: '4px' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                            <FileAudio size={16} />
                            <span>{ds.name}</span>
                            <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>({ds.format})</span>
                        </div>
                        <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>{ds.upload_time}</span>
                    </div>
                ))}
            </div>
        </div>
    );
};
