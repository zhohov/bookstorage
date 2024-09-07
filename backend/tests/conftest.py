import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, clear_mappers

from src.infrastructure.persistence.tables import metadata, start_mappers


@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    return engine


@pytest.fixture
def session_factory(in_memory_db):
    start_mappers()
    yield sessionmaker(bind=in_memory_db)
    clear_mappers()

@pytest.fixture
def session(session_factory) -> Session:
    return session_factory()

