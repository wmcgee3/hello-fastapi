from fastapi import APIRouter

from ..schemas import Link
from .schemas import HelloResponse

hello = APIRouter(prefix="/hello")


@hello.get("")
def stuff_root():
    return HelloResponse(
        _links=[Link(rel="self", href=hello.prefix)],
        message="Hello from FastAPI!",
    )
