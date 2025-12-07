from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ..core.logging import logger

app = FastAPI(
    title="Promethium API",
    description="API for Seismic Data Recovery Framework",
    version="0.1.0"
)

# CORS configuration
origins = [
    "http://localhost",
    "http://localhost:5173", # Vite default
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to Promethium API"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}
