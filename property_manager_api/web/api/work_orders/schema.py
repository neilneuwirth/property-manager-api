from pydantic import BaseModel


class MaintenaceRequestText(BaseModel):
    """Simple maintenance request message."""
    message: str

class MaintenaceRequest(BaseModel):
    """Simple maintenance request model."""
    data: dict