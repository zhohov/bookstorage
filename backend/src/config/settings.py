import os
from dataclasses import dataclass, field


@dataclass
class DatabaseSettings:
    db_name: str = field(default=os.getenv("DB_NAME", "example"))
    db_user: str = field(default=os.environ.get("DB_USER", "postgres"))
    db_password: str = field(default=os.getenv("DB_PASSWORD", "postgres"))
    db_host: str = field(default=os.getenv("DB_HOST", "db"))
    db_port: str = field(default=os.getenv("DB_PORT", "5432"))

    @property
    def url(self) -> str:
        return f"postgresql+psycopg2://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"  # noqa: E501


@dataclass
class Settings:
    db: DatabaseSettings = field(default_factory=DatabaseSettings)
    api_url: str = field(default=os.getenv("API_URL"))


settings = Settings()

