from fastapi import APIRouter, HTTPException

from ..schemas import Link
from .items import ITEMS
from .schemas import ThingResponse, ThingsResponse

things = APIRouter(prefix="/things")


@things.get("", response_model=ThingsResponse)
def things_root():
    return ThingsResponse(
        _links=[Link(rel="self", href=things.prefix)],
        items=[
            ThingResponse(
                _links=[Link(rel="self", href=f"{things.prefix}/{name}")],
                name=name,
                color=color,
            )
            for name, color in ITEMS.items()
        ],
    )


@things.get("/{name}")
def get_thing(name: str):
    color = ITEMS.get(name)
    if color is None:
        raise HTTPException(404, f"thing not found")
    return ThingResponse(
        _links=[Link(rel="self", href=f"{things.prefix}/{name}")],
        name=name,
        color=color,
    )
