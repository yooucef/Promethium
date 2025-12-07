import { useState, useEffect } from 'react';
import { fetchDatasets, fetchJobs, createJob, type Job, type Dataset } from '../api/client';
import { Play, Activity } from 'lucide-react';

export const JobManager = () => {
    const [jobs, setJobs] = useState<Job[]>([]);
    const [datasets, setDatasets] = useState<Dataset[]>([]);

    useEffect(() => {
        fetchJobs().then(setJobs);
        fetchDatasets().then(setDatasets);
        const interval = setInterval(() => fetchJobs().then(setJobs), 3000);
        return () => clearInterval(interval);
    }, []);

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        const formData = new FormData(e.currentTarget);
        const datasetId = parseInt(formData.get('dataset_id') as string);
        const algorithm = formData.get('algorithm') as string;

        try {
            await createJob(datasetId, algorithm, {});
            const data = await fetchJobs();
            setJobs(data);
        } catch (err) {
            alert('Job submission failed');
        }
    };

    const getStatusClass = (status: string) => {
        switch (status) {
            case 'RUNNING': return 'status-run';
            case 'COMPLETED': return 'status-com';
            case 'FAILED': return 'status-fail';
            default: return 'status-que';
        }
    };

    return (
        <div className="card">
            <h2>Processing Jobs</h2>

            <form onSubmit={handleSubmit} style={{ display: 'grid', gridTemplateColumns: '1fr 1fr auto', gap: '1rem', marginBottom: '2rem' }}>
                <select name="dataset_id" className="input" required>
                    <option value="">Select Dataset...</option>
                    {datasets.map(ds => <option key={ds.id} value={ds.id}>{ds.name}</option>)}
                </select>
                <select name="algorithm" className="input">
                    <option value="unet">U-Net Reconstruction</option>
                    <option value="matrix_completion">Matrix Completion</option>
                    <option value="deconvolution">Deconvolution</option>
                </select>
                <button type="submit" className="btn">
                    <Play size={18} />
                    Start Job
                </button>
            </form>

            <div style={{ display: 'grid', gap: '0.5rem' }}>
                {jobs.map(job => (
                    <div key={job.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '0.75rem', background: 'var(--bg-tertiary)', borderRadius: '4px' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                            <Activity size={16} />
                            <span style={{ fontFamily: 'monospace' }}>{job.id.slice(0, 8)}</span>
                            <span className={`status-badge ${getStatusClass(job.status)}`}>{job.status}</span>
                        </div>
                        <div>
                            <span style={{ marginRight: '1rem' }}>{job.algorithm}</span>
                            <small style={{ color: 'var(--text-secondary)' }}>{new Date(job.created_at).toLocaleTimeString()}</small>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};
