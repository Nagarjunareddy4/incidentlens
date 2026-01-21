from datetime import datetime
from typing import Optional, Dict
from pydantic import BaseModel, Field


class Alert(BaseModel):
    alert_name: str
    severity: str
    service: str
    instance: str
    starts_at: datetime
    summary: str
    description: Optional[str] = None
    labels: Dict[str, str] = Field(default_factory=dict)
