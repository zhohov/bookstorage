import pytest
import time
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, clear_mappers

from src.infrastructure.persistence.tables import metadata, start_mappers
from src.domain.entities import Author
from src.domain.value_objects import FullName


@pytest.fixture
def author() -> Author:
    fullname = FullName(first_name="John", last_name="Doe")
    author = Author(fullname=fullname, biography="A famous author")

    return author


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


def wait_for_webapp_to_come_up():
    deadline = time.time() + 10
    url = "http://backend_test:8000/"
    while time.time() < deadline:
        try:
            return requests.get(url)
        except ConnectionError:
            time.sleep(0.5)
    pytest.fail("API never came up")


@pytest.fixture
def restart_api():
    time.sleep(2)
    wait_for_webapp_to_come_up()

