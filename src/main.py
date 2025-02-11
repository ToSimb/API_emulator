from fastapi import FastAPI

from freon.router import router as router_freon
from at.router import router as router_at

def get_application() -> FastAPI:
    application = FastAPI(
        title="API emulator",
    )
    return application


app = get_application()

app.include_router(router_freon)

app.include_router(router_at)