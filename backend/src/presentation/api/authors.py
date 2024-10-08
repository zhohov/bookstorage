from typing import Any, Dict, List, Optional
from uuid import UUID
from fastapi import APIRouter, HTTPException, status
from fastapi.requests import Request
from src.application.services.services import AuthorService
from src.application.dto.dto import AuthorInput, AuthorOutput
from src.infrastructure.persistence.uow import SqlAlchemyUnitOfWork


authors_router = APIRouter(
    prefix="/authors",
    tags=["author"],
)


@authors_router.get(path="/", status_code=status.HTTP_200_OK)
def get_all_authors(request: Request) -> Optional[List[AuthorOutput]]:
    uow = SqlAlchemyUnitOfWork()
    service = AuthorService(uow=uow)

    authors = service.all()

    return authors


@authors_router.get(path="/{id}", status_code=status.HTTP_200_OK)
def get_author_by_id(request: Request, id: UUID) -> Optional[AuthorOutput]:
    uow = SqlAlchemyUnitOfWork()
    service = AuthorService(uow=uow)

    author = service.get_by_id(id=id)

    if not author:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

    return author
    

@authors_router.post(path="/", status_code=status.HTTP_201_CREATED)
def create_author(request: Request, payload: AuthorInput) -> Dict[str, Any]:
    uow = SqlAlchemyUnitOfWork()
    service = AuthorService(uow=uow)

    author = service.create(payload=payload)

    return {"created": AuthorOutput(**author.to_dict())}

