from pydantic import BaseModel, Field


class Link(BaseModel):
    rel: str
    href: str


class RootResponse(BaseModel):
    links: list[Link] = Field(..., alias="_links")
