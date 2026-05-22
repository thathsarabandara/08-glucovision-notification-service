from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from app.models.base import Base

class NotificationLog(Base):
    __tablename__ = "notification_logs"

    id = Column(Integer, primary_key=True, index=True)
    notification_id = Column(Integer, ForeignKey("notifications.id"), nullable=False)
    status = Column(String(50), nullable=False) # success, failed
    provider_response = Column(Text, nullable=True)
    error_message = Column(Text, nullable=True)
    attempt_count = Column(Integer, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
