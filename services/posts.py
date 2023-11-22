from models.post import Post
from schemas.posts import PostCreateDto, PostUpdateDto
from services.base import RepositoryDB


class PostsRepository(RepositoryDB[Post, PostCreateDto, PostUpdateDto]):
    ...


posts_crud = PostsRepository(Post)
