# =============================================================================
# Promethium Backend Dockerfile - Optimized Build
# =============================================================================
# Uses Miniconda for pre-compiled scientific packages (numpy, scipy, pytorch)
# Build time: ~3-4 minutes first build, <20 seconds for cached rebuilds
# =============================================================================

# -----------------------------------------------------------------------------
# Stage 1: Conda Environment Builder
# -----------------------------------------------------------------------------
FROM continuumio/miniconda3:24.1.2-0 AS conda-builder

WORKDIR /build

# Copy conda environment file first for optimal caching
COPY docker/environment.yml .

# Create conda environment with pre-compiled scientific packages
# Using --no-default-packages to minimize size
RUN conda env create -f environment.yml -n promethium && \
    conda clean -afy && \
    find /opt/conda/envs/promethium -name "*.pyc" -delete && \
    find /opt/conda/envs/promethium -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true

# -----------------------------------------------------------------------------
# Stage 2: Pip Dependencies
# -----------------------------------------------------------------------------
FROM conda-builder AS pip-builder

# Copy pip requirements for lightweight packages
COPY docker/requirements.txt .

# Install pip packages into conda environment
RUN /opt/conda/envs/promethium/bin/pip install --no-cache-dir -r requirements.txt

# Copy source code and install the package
COPY pyproject.toml README.md ./
COPY src/ src/

RUN /opt/conda/envs/promethium/bin/pip install --no-cache-dir .

# -----------------------------------------------------------------------------
# Stage 3: Runtime Image (Minimal)
# -----------------------------------------------------------------------------
FROM debian:bookworm-slim AS runtime

WORKDIR /app

# Install minimal runtime dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq5 \
    libgomp1 \
    curl \
    ca-certificates && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get clean

# Copy conda environment from builder
COPY --from=pip-builder /opt/conda/envs/promethium /opt/conda/envs/promethium

# Set up environment variables
ENV PATH="/opt/conda/envs/promethium/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# Copy application source
COPY --from=pip-builder /build/src /app/src

# Create non-root user for security
RUN useradd -m -u 1000 promethium && \
    chown -R promethium:promethium /app
USER promethium

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Default port
EXPOSE 8000

# Default command
CMD ["uvicorn", "promethium.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
