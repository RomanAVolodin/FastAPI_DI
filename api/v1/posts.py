from typing import Annotated

from fastapi import APIRouter, Depends, Query

from schemas.posts import PostResponseDto, PostCreateDto
from services.posts import PostsServiceABC

router = APIRouter()


@router.get('/', response_model=list[PostResponseDto])
async def get_posts(
    *,
    service: PostsServiceABC = Depends(),
    skip: Annotated[int, Query(description='Items to skip', ge=0)] = 0,
    limit: Annotated[int, Query(description='Pagination page size', ge=1)] = 10,
) -> list[PostResponseDto]:
    entities = await service.get_multy(skip=skip, limit=limit)
    return entities


@router.post('/', response_model=PostResponseDto)
async def add_post(
    *,
    service: PostsServiceABC = Depends(),
    post_dto: PostCreateDto,
) -> PostResponseDto:
    post = await service.create(dto=post_dto)
    return post
