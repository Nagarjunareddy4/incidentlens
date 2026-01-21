from app.models.alert import Alert
from datetime import datetime
from pydantic import BaseModel

class NormalizedAlert(BaseModel):
    alert_name: str
    severity: str
    service: str
    instance: str
    starts_at: datetime
    summary: str
    description: str | None = None
    labels: dict[str, str]