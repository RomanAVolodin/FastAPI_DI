from abc import ABC, abstractmethod
from typing import Any, Generic, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from db.db import Base

ModelType = TypeVar('ModelType', bound=Base)
CreateSchemaType = TypeVar('CreateSchemaType', bound=BaseModel)
UpdateSchemaType = TypeVar('UpdateSchemaType', bound=BaseModel)


class Repository(ABC):
    @abstractmethod
    def get(self, *args, **kwargs):
        ...

    @abstractmethod
    def get_multi(self, *args, **kwargs):
        ...

    @abstractmethod
    def create(self, *args, **kwargs):
        ...

    @abstractmethod
    def update(self, *args, **kwargs):
        ...

    @abstractmethod
    def delete(self, *args, **kwargs):
        ...


class RepositoryDB(Repository, Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType], db: AsyncSession):
        self._model = model
        self.db = db

    async def get(self, id: Any) -> ModelType | None:
        statement = select(self._model).where(self._model.id == id)
        results = await self.db.execute(statement=statement)
        return results.scalar_one_or_none()

    async def get_multi(self, *, skip=0, limit=100) -> list[ModelType]:
        statement = select(self._model).offset(skip).limit(limit)
        results = await self.db.execute(statement=statement)
        return results.scalars().all()

    async def create(self, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self._model(**obj_in_data)
        self.db.add(db_obj)
        await self.db.commit()
        return db_obj

    async def update(
        self, *, db_obj: ModelType, obj_in: UpdateSchemaType | dict[str, Any]
    ) -> ModelType:
        # todo
        return db_obj

    async def delete(self, *, id: int) -> ModelType:
        # todo
        db_obj = None
        return db_obj
