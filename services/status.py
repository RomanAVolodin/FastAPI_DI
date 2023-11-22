from schemas.status import StatusResponse


class StatusService:
    async def get_api_status(self) -> StatusResponse:
        return StatusResponse(api=True)


def get_status_service() -> StatusService:
    return StatusService()
