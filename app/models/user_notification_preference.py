from sqlalchemy import Column, String, Integer, DateTime, JSON, Boolean
from sqlalchemy.sql import func
from app.models.base import Base

class UserNotificationPreferenceCache(Base):
    __tablename__ = "user_notification_preferences_cache"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(255), unique=True, index=True, nullable=False)
    email_enabled = Column(Boolean, default=True)
    push_enabled = Column(Boolean, default=True)
    quiet_hours_start = Column(String(5), nullable=True) # e.g., "22:00"
    quiet_hours_end = Column(String(5), nullable=True)   # e.g., "07:00"
    preferred_language = Column(String(10), default="en")
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
