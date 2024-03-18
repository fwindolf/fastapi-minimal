from fastapi import FastAPI

from api.home import router as home_router
from api.v1.protected import router as protected_router

app = FastAPI()

app.include_router(home_router)
app.include_router(protected_router, prefix="/v1")
