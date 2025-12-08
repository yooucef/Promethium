import { Routes } from '@angular/router';
import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { JobSubmissionComponent } from './pages/job-submission/job-submission.component';
import { VisualizationComponent } from './pages/visualization/visualization.component';

export const routes: Routes = [
    { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
    { path: 'dashboard', component: DashboardComponent },
    { path: 'jobs', component: JobSubmissionComponent },
    { path: 'visualize', component: VisualizationComponent },
    { path: '**', redirectTo: '/dashboard' }
];
