import { Routes } from '@angular/router';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { JobSubmissionComponent } from './pages/job-submission/job-submission.component';
import { VisualizationComponent } from './pages/visualization/visualization.component';
import { DatasetsComponent } from './pages/datasets/datasets.component';
import { SettingsComponent } from './pages/settings/settings.component';
import { ModelsComponent } from './pages/models/models.component';
import { ResultsComponent } from './pages/results/results.component';
import { SystemComponent } from './pages/system/system.component';
import { DocsComponent } from './pages/docs/docs.component';
import { PipelinesComponent } from './pages/pipelines/pipelines.component';
import { ExperimentsComponent } from './pages/experiments/experiments.component';
import { BenchmarksComponent } from './pages/benchmarks/benchmarks.component';
import { authGuard } from './core/guards/auth.guard';

export const routes: Routes = [
    { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
    { path: 'dashboard', component: DashboardComponent, canActivate: [authGuard] },
    { path: 'datasets', component: DatasetsComponent, canActivate: [authGuard] },
    { path: 'jobs', component: JobSubmissionComponent, canActivate: [authGuard] },
    { path: 'pipelines', component: PipelinesComponent, canActivate: [authGuard] },
    { path: 'models', component: ModelsComponent, canActivate: [authGuard] },
    { path: 'experiments', component: ExperimentsComponent, canActivate: [authGuard] },
    { path: 'benchmarks', component: BenchmarksComponent, canActivate: [authGuard] },
    { path: 'results', component: ResultsComponent, canActivate: [authGuard] },
    { path: 'system', component: SystemComponent, canActivate: [authGuard] },
    { path: 'docs', component: DocsComponent }, // Docs might be public
    { path: 'visualize', component: VisualizationComponent, canActivate: [authGuard] },
    { path: 'settings', component: SettingsComponent, canActivate: [authGuard] },
    { path: '**', redirectTo: '/dashboard' }
];
