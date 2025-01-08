from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from typing import Generator
from src.core.config import settings
import logging

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

logger = logging.getLogger(__name__)

def get_db() -> Generator:
	db = SessionLocal()
	try:
		yield db
	except SQLAlchemyError as e:
		logger.error(f"Database error: {str(e)}")
		db.rollback()
		raise
	finally:
		db.close()