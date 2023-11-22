from functools import cache

from dependencies.registrator import add_factory_to_mapper

from services.status import StatusServiceABC, StatusService


@add_factory_to_mapper(StatusServiceABC)
@cache
def create_status_service() -> StatusService:
    return StatusService()
