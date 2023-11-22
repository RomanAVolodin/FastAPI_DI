import logging

import uvicorn
from fastapi import FastAPI

from api.v1.posts import router as router_posts
from api.v1.status import router as router_status
from core.logger import LOGGING
from core.settings import settings
from db.db import create_database
from dependencies.main import setup_dependencies

app = FastAPI(
    title=settings.project_name,
    description=settings.project_description,
    version='1.0.0',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)


@app.on_event('startup')
async def startup():
    if settings.debug_mode:
        from models.post import Post  # noqa: F401

        await create_database()


app.include_router(router_posts, prefix='/api/v1/posts')
app.include_router(router_status, prefix='/api/v1/status')

setup_dependencies(app)


if __name__ == '__main__':
    uvicorn.run(
        'main:app', host='0.0.0.0', port=settings.app_port, log_config=LOGGING, log_level=logging.DEBUG, reload=True,
    )
