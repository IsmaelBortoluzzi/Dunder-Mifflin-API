from pydantic import BaseModel, Field
from datetime import datetime


class ErrorMessage(BaseModel):
    message: str = Field(exemple="Error")