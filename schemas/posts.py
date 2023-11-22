from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class PostCreateDto(BaseModel):
    subject: str
    text: str


class PostUpdateDto(BaseModel):
    subject: str
    text: str


class PostResponseDto(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    subject: str
    text: str
    created_at: datetime
