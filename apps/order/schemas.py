from pydantic import BaseModel, Field
from datetime import datetime


class Order(BaseModel):
    id: int
    user_id: int
    total: float
    obs: str
    create_date: datetime
    update_date: datetime
