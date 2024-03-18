from fastapi import HTTPException, Security
from fastapi.security import api_key

from api.settings import settings

api_key_header = api_key.APIKeyHeader(name="X-API-KEY")


async def validate_api_key(key: str = Security(api_key_header)):
    if key != settings.api_key:
        raise HTTPException(status_code=401, detail="Invalid or missing Api Key")

    return None
