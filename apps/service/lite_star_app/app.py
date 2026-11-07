from litestar import Litestar, get


@get("/")
async def hello() -> dict[str, str]:
    return {"message": "Hello, world!"}


app = Litestar(route_handlers=[hello])
