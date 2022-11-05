from pydantic import BaseModel, Field

from ..schemas import Link


class HelloResponse(BaseModel):
    links: list[Link] = Field(alias="_links")
    message: str
