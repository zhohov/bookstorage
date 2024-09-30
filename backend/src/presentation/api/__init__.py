__all__ = ("authors_router", "books_router", "routers")

from .authors import authors_router
from .books import books_router

routers = [authors_router, books_router]
