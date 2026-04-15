from pydantic import BaseModel
from typing import Optional

class TicketCreate(BaseModel):
    title: str
    description: str
    priority: str
    category: str

class TicketUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    category: Optional[str] = None