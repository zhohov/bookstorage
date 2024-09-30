from typing import List, Optional
from uuid import UUID
from fastapi import APIRouter, status, HTTPException
from fastapi.requests import Request

from application.dto.dto import BookOutput, BookInput
from application.services.services import BookService
from domain.entities import Book
from infrastructure.persistence.uow import SqlAlchemyUnitOfWork

books_router = APIRouter(
    prefix="/books",
    tags=["book"]
)


@books_router.get(path="/", status_code=status.HTTP_200_OK)
def get_all_books(request: Request) -> Optional[List[BookOutput]]:
    uow = SqlAlchemyUnitOfWork()
    service = BookService(uow=uow)

    books = service.all()

    return books


@books_router.post(path="/", status_code=status.HTTP_201_CREATED)
def create_book(request: Request, payload: BookInput) -> BookOutput:
    uow = SqlAlchemyUnitOfWork()
    service = BookService(uow=uow)

    book = service.create(payload=payload)

    return {BookOutput(**book.to_dict())}


@books_router.get(path="/{id}")
def get_book(request: Request, id: UUID) -> Optional[BookOutput]:
    uow = SqlAlchemyUnitOfWork()
    service = BookService(uow=uow)

    book = service.get(key="id", value=id)

    if not book:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)

    return book


