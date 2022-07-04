from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from core.config import settings
import logging


_logger = logging.getLogger("uvicorn.error")

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
_logger.debug(f"database url: {SQLALCHEMY_DATABASE_URL}")

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
