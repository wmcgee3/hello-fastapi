from fastapi import FastAPI

from .schemas import RootResponse, Link
from .stuff.router import stuff

app = FastAPI()


@app.get("/", response_model=RootResponse)
def app_root():
    return RootResponse(
        _links=[
            Link(rel="self", href="/"),
            Link(rel="stuff", href="/stuff"),
        ],
    )


app.include_router(stuff)
