from src.config import settings

def test_database_settings() -> None:
    db_url: str = "postgresql+asyncpg://postgres:postgres@db:5432/example"
    
    assert db_url == settings.db.url

