import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime, UUID

from db.db import Base


class Post(Base):
    __tablename__ = 'posts'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    subject = Column(String(255), nullable=False, unique=True)
    text = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
