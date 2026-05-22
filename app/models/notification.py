from sqlalchemy import Column, String, Integer, DateTime, JSON, Text, ForeignKey
from sqlalchemy.sql import func
from app.models.base import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(255), index=True, nullable=False)
    type = Column(String(50), nullable=False) # e.g., email, push, sms
    status = Column(String(50), default="pending") # pending, sent, failed
    subject = Column(String(255), nullable=True)
    content = Column(Text, nullable=False)
    metadata_json = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
