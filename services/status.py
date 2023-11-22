from abc import ABC, abstractmethod

from schemas.status import StatusResponse


class StatusServiceABC(ABC):
    @abstractmethod
    async def get_api_status(self) -> StatusResponse:
        ...


class StatusService(StatusServiceABC):
    async def get_api_status(self) -> StatusResponse:
        return StatusResponse(api=True)

