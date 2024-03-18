from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def home():
    return {"message": "Hello World!"}


@router.get("/health")
async def healthcheck():
    return {"status": "ok"}
