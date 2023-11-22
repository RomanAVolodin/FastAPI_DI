from pydantic import BaseModel


class StatusResponse(BaseModel):
    api: bool
