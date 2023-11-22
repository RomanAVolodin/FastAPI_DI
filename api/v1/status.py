import logging

from fastapi import APIRouter, Depends, status

from schemas.status import StatusResponse
from services.status import get_status_service, StatusService

router = APIRouter(prefix='/status', tags=['Status'])

logger = logging.getLogger().getChild('status-router')


@router.get(
    '',
    summary='Получить статус API',
    response_model=StatusResponse,
    status_code=status.HTTP_200_OK,
)
async def _get_api_status(
    status_service: StatusService = Depends(get_status_service),
) -> StatusResponse:
    logger.debug('Get api status')
    return await status_service.get_api_status()
