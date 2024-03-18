from fastapi import APIRouter, Depends

from api import auth

router = APIRouter(dependencies=[Depends(auth.validate_api_key)])


@router.get("/protected")
async def secret():
    return {"message": "This is some protected information"}
