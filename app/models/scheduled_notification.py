from sqlalchemy import Column, String, Integer, DateTime, JSON, ForeignKey
from sqlalchemy.sql import func
from app.models.base import Base

class ScheduledNotification(Base):
    __tablename__ = "scheduled_notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(255), index=True, nullable=False)
    template_name = Column(String(100), nullable=False)
    scheduled_time = Column(DateTime(timezone=True), nullable=False)
    status = Column(String(50), default="pending") # pending, processed, cancelled
    metadata_json = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
