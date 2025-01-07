import logging
from .session import engine
from .base import Base
# Import all models here
from src.models.user import User  # noqa: F401

logger = logging.getLogger(__name__)

def init_db() -> None:
    try:
        # Create all tables
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {str(e)}")
        raise
