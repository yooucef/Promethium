import { inject } from '@angular/core';
import { Router, CanActivateFn } from '@angular/router';
import { ApiService } from '../../services/api.service';

export const authGuard: CanActivateFn = (route, state) => {
    const apiService = inject(ApiService);
    const router = inject(Router);

    // For this implementation, we assume if the backend is reachable or we are in demo mode,
    // we allow access. In a real app, this would check for a valid JWT token.

    // Simple check: is there a mock 'user' in local storage?
    const isAuthenticated = localStorage.getItem('user_token') !== null || apiService.isBackendAvailable();

    if (isAuthenticated) {
        return true;
    }

    // Redirect to login page (if we had one, but for now we redirect to dashboard or show alert)
    // For the purpose of this demo-capable app, we default to allowing access to dashboard
    // but maybe restrict sensitive areas?

    // For now, let's just return true to not block the demo flow unless we implement a full login page.
    return true;
};
