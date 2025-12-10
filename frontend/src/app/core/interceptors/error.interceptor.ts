import { HttpInterceptorFn, HttpErrorResponse } from '@angular/common/http';
import { inject } from '@angular/core';
import { throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { ApiService } from '../../services/api.service';

export const errorInterceptor: HttpInterceptorFn = (req, next) => {
    const apiService = inject(ApiService);

    return next(req).pipe(
        catchError((error: HttpErrorResponse) => {
            let errorMsg = '';

            if (error.status === 401) {
                // Unauthorized
                console.warn('Unauthorized request');
                // Could redirect to login here
            } else if (error.status === 403) {
                // Forbidden
                console.error('Access forbidden');
            } else if (error.status === 0) {
                // Network error / Offline
                console.error('Network error - Backend might be down');
            }

            return throwError(() => error);
        })
    );
};
