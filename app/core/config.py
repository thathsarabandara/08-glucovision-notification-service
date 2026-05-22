from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional, List, Union
from pydantic import AnyHttpUrl, validator

class Settings(BaseSettings):
    PROJECT_NAME: str = "GlucoVision Notification Service"
    API_V1_STR: str = "/api/v1"
    
    # Database (MySQL Async)
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "password"
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_DB: str = "glucovision_notification_db"
    
    @property
    def ASYNC_DATABASE_URI(self) -> str:
        return f"mysql+aiomysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"

    # Redis (For Celery/Rate Limiting)
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    
    @property
    def REDIS_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/0"

    # Kafka (Event Bus)
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    KAFKA_NOTIFICATION_TOPIC: str = "notifications"

    # Email Settings
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = 587
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[str] = None
    EMAILS_FROM_NAME: Optional[str] = "GlucoVision System"

    # Firebase Settings (Path to service account JSON)
    FIREBASE_CREDENTIALS_PATH: Optional[str] = None

    model_config = SettingsConfigDict(case_sensitive=True, env_file=".env")

settings = Settings()
