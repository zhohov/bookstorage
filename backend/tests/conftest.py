import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, clear_mappers

from infrastructure.database.session import FakeSession
from src.infrastructure.database.tables import metadata, start_mappers


@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    return engine


@pytest.fixture
def session(in_memory_db):
    start_mappers()
    yield sessionmaker(bind=in_memory_db)()
    clear_mappers()


@pytest.fixture
def fake_session() -> Session:
    return FakeSession()

