class PromethiumError(Exception):
    """Base exception for Promethium."""
    pass

class DataIngestionError(PromethiumError):
    """Raised when data ingestion fails."""
    pass

class MetadataError(PromethiumError):
    """Raised when metadata validation fails."""
    pass

class ProcessingError(PromethiumError):
    """Raised when a signal processing operation fails."""
    pass
