import uvicorn
from fastapi import FastAPI

from src.infrastructure.application.factory import create_app
from src.infrastructure.persistence.tables import start_mappers, metadata
from src.infrastructure.persistence.session import get_engine
from src.presentation.api import routers


app: FastAPI = create_app(
    title="bookstorage",
    routers=routers,
)


@app.on_event("startup")
def startup_event() -> None:
    metadata.create_all(bind=get_engine())
    start_mappers()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

