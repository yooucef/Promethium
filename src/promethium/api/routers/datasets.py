from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
import shutil
import os
from uuid import uuid4

from promethium.core.database import get_db, Dataset
from promethium.core.schemas import DatasetRead, DatasetCreate
from promethium.core.config import get_settings
from promethium.core.logging import logger

router = APIRouter(prefix="/datasets", tags=["datasets"])
settings = get_settings()

@router.post("/", response_model=DatasetRead, status_code=201)
async def create_dataset(
    name: str = Form(...),
    format: str = Form(...),
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):
    """
    Upload and register a new dataset.
    """
    # Ensure storage exists
    os.makedirs(settings.DATA_STORAGE_PATH, exist_ok=True)
    
    # Save file
    file_id = str(uuid4())
    filename = f"{file_id}_{file.filename}"
    file_path = os.path.join(settings.DATA_STORAGE_PATH, filename)
    
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        logger.error(f"File upload failed: {e}")
        raise HTTPException(status_code=500, detail="File upload failed")

    # Create DB record
    new_dataset = Dataset(
        name=name,
        format=format,
        file_path=file_path,
        metadata_json={}
    )
    db.add(new_dataset)
    await db.commit()
    await db.refresh(new_dataset)
    
    logger.info(f"Dataset registered: {new_dataset.id}")
    return new_dataset

@router.get("/", response_model=List[DatasetRead])
async def list_datasets(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Dataset).offset(skip).limit(limit))
    datasets = result.scalars().all()
    return datasets

@router.get("/{dataset_id}", response_model=DatasetRead)
async def get_dataset(dataset_id: int, db: AsyncSession = Depends(get_db)):
    dataset = await db.get(Dataset, dataset_id)
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return dataset
