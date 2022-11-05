from pydantic import BaseModel, Field

from ..schemas import Link


class StuffResponse(BaseModel):
    links: list[Link] = Field(..., alias="_links")
    items: list[str]
