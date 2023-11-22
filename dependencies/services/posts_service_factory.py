from functools import cache

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_db_session
from dependencies.registrator import add_factory_to_mapper
from models import Post
from services.posts import PostsServiceABC, PostsService, PostsRepository


@add_factory_to_mapper(PostsServiceABC)
@cache
def create_posts_service(
    session: AsyncSession = Depends(get_db_session),
) -> PostsService:
    return PostsService(repository=PostsRepository(Post, db=session))
