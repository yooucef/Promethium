# =============================================================================
# Promethium Frontend Dockerfile - Optimized Build
# =============================================================================
# Uses Node.js 20 Alpine for Angular 21+ compatibility
# Build time: ~1-2 minutes first build, <10 seconds for cached rebuilds
# =============================================================================

# -----------------------------------------------------------------------------
# Stage 1: Dependencies Installation
# -----------------------------------------------------------------------------
FROM node:20-alpine AS deps

WORKDIR /app

# Copy package files first for optimal caching
COPY package.json package-lock.json ./

# Install dependencies with clean install
# Using --prefer-offline to use cache when available
RUN npm ci --prefer-offline --no-audit --no-fund

# -----------------------------------------------------------------------------
# Stage 2: Build Application
# -----------------------------------------------------------------------------
FROM node:20-alpine AS builder

WORKDIR /app

# Copy installed dependencies from deps stage
COPY --from=deps /app/node_modules ./node_modules

# Copy source code
COPY . .

# Build production bundle
# Angular CLI automatically uses caching in node_modules/.angular
RUN npm run build -- --configuration production

# -----------------------------------------------------------------------------
# Stage 3: Production Runtime (Nginx)
# -----------------------------------------------------------------------------
FROM nginx:alpine AS runtime

# Remove default nginx content
RUN rm -rf /usr/share/nginx/html/*

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy built Angular application
COPY --from=builder /app/dist/web/browser /usr/share/nginx/html

# Add non-root user for security
RUN adduser -D -u 1000 nginx-user && \
    chown -R nginx-user:nginx-user /usr/share/nginx/html && \
    chown -R nginx-user:nginx-user /var/cache/nginx && \
    touch /var/run/nginx.pid && \
    chown -R nginx-user:nginx-user /var/run/nginx.pid

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --quiet --tries=1 --spider http://localhost:80/ || exit 1

# Expose port
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
