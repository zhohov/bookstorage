from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4
from fastapi import APIRouter, status
from fastapi.requests import Request
from src.application.services.services import AuthorService
from src.application.dto.dto import AuthorInput, AuthorOutput
from src.infrastructure.persistence.uow import SqlAlchemyUnitOfWork


authors_router = APIRouter(
    prefix="/authors",
    tags=["author"],
)


@authors_router.get(path="/{id}", status_code=status.HTTP_200_OK)
def get_author(request: Request, id: UUID) -> AuthorOutput:
    uow = SqlAlchemyUnitOfWork()
    service = AuthorService(uow=uow)

    retrieved_author = service.get(key="id", value=id)

    author = AuthorOutput(**retrieved_author.to_dict())

    return author
    

@authors_router.post(path="/", status_code=status.HTTP_201_CREATED)
def create_author(request: Request, payload: AuthorInput) -> Dict[str, Any]:
    uow = SqlAlchemyUnitOfWork()
    service = AuthorService(uow=uow)

    author = service.create(payload=payload)

    return {"created": AuthorOutput(**author.to_dict())}


@authors_router.post(path="/all", status_code=status.HTTP_200_OK)
def create_author(request: Request) -> Optional[List[AuthorOutput]]:
    uow = SqlAlchemyUnitOfWork()
    service = AuthorService(uow=uow)

    authors = service.all()

    return authors


