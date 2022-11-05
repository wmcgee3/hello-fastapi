from fastapi import APIRouter

from ..schemas import Link
from .schemas import StuffResponse

stuff = APIRouter(prefix="/stuff")


@stuff.get("")
def stuff_root():
    return StuffResponse(
        _links=[Link(rel="self", href=stuff.prefix)],
        items=[
            "one",
            "two",
            "red",
            "blue",
        ],
    )
