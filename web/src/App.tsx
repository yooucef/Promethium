import { DatasetManager } from './components/DatasetManager';
import { JobManager } from './components/JobManager';
import { Layers } from 'lucide-react';
import './App.css';

function App() {
  return (
    <div>
      <header style={{ padding: '1rem 2rem', borderBottom: '1px solid var(--border)', display: 'flex', alignItems: 'center', gap: '1rem' }}>
        <Layers size={32} color="var(--accent-primary)" />
        <h1 style={{ fontSize: '1.5rem', margin: 0 }}>Promethium Framework</h1>
      </header>

      <main className="container">
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '2rem' }}>
          <DatasetManager />
          <JobManager />
        </div>

        <div className="card" style={{ marginTop: '2rem', height: '400px', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--text-secondary)' }}>
          <div>[Interactive Seismic Visualization Area - Coming Soon]</div>
        </div>
      </main>
    </div>
  );
}

export default App;
