from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID

from models.post import Post
from schemas.posts import PostCreateDto, PostUpdateDto
from services.base import RepositoryDB


class PostsRepository(RepositoryDB[Post, PostCreateDto, PostUpdateDto]):
    ...


class PostsServiceABC(ABC):
    @abstractmethod
    async def get(self, id: Any) -> list[Post]:
        ...

    @abstractmethod
    async def get_multy(self, skip: int, limit: int) -> list[Post]:
        ...

    @abstractmethod
    async def create(self, dto: PostCreateDto) -> Post:
        ...


class PostsService(PostsServiceABC):
    def __init__(self, repository: PostsRepository) -> None:
        self._repository = repository

    async def get(self, id: UUID) -> Post:
        return await self._repository.get(id)

    async def get_multy(self, skip: int, limit: int) -> list[Post]:
        return await self._repository.get_multi(skip=skip, limit=limit)

    async def create(self, dto: PostCreateDto) -> Post:
        return await self._repository.create(obj_in=dto)
