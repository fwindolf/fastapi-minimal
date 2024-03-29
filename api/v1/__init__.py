from fastapi import APIRouter

from api.v1.protected import router as protected_router

router = APIRouter()
router.include_router(protected_router)
