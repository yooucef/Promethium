from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from promethium.core.config import get_settings
from promethium.core.logging import logger
from promethium.core.database import engine, Base
from promethium.api.routers import datasets, jobs

settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create DB tables if not exist (dev mode)
    # In production, recommend using Alembic migrations
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database initialized.")
    yield
    # Shutdown
    logger.info("Shutting down.")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
origins = ["*"] # Configure appropriately for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(datasets.router, prefix=settings.API_PREFIX)
app.include_router(jobs.router, prefix=settings.API_PREFIX)

@app.get("/health")
async def health_check():
    return {"status": "ok", "version": settings.APP_VERSION}
