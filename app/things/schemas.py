from pydantic import BaseModel, Field

from ..schemas import Link


class ThingResponse(BaseModel):
    links: list[Link] = Field(alias="_links")
    name: str
    color: str


class ThingsResponse(BaseModel):
    links: list[Link] = Field(alias="_links")
    items: list[ThingResponse]
