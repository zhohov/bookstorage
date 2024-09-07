from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

from src.config import settings


def get_engine() -> Engine:
    return create_engine(url=settings.db.url, echo=True)


DEFAULT_SESSION_FACTORY = sessionmaker(bind=get_engine())

