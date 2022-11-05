from fastapi import FastAPI

from .schemas import RootResponse, Link
from .hello.router import hello
from .things.router import things

app = FastAPI()


@app.get("/", response_model=RootResponse)
def app_root():
    return RootResponse(
        _links=[
            Link(rel="self", href="/"),
            Link(rel="hello", href=hello.prefix),
            Link(rel="things", href=things.prefix),
        ],
    )


app.include_router(hello)
app.include_router(things)
