from typing import Annotated

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from db.db import get_session
from schemas.posts import PostResponseDto, PostCreateDto
from services.posts import posts_crud

router = APIRouter()


@router.get('/', response_model=list[PostResponseDto])
async def get_posts(
    *,
    db: AsyncSession = Depends(get_session),
    skip: Annotated[int, Query(description='Items to skip', ge=0)] = 0,
    limit: Annotated[int, Query(description='Pagination page size', ge=1)] = 10,
) -> list[PostResponseDto]:
    entities = await posts_crud.get_multi(db=db, skip=skip, limit=limit)
    return entities


@router.post('/', response_model=PostResponseDto)
async def add_post(
    *,
    db: AsyncSession = Depends(get_session),
    post_dto: PostCreateDto,
) -> PostResponseDto:
    post = await posts_crud.create(db=db, obj_in=post_dto)
    return post
