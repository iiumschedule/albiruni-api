from typing import Optional
from pydantic import BaseModel, Field


# properties required during user creation
class ExamDateTime(BaseModel):
    date: str = Field(None, description="Exam date", example="30-JAN-23")
    time: str = Field(None, description="Exam time", example="9.00 AM")
