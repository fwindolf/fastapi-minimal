from fastapi.testclient import TestClient
from pydantic_settings import BaseSettings


def test_protected(client: TestClient, settings: BaseSettings):
    response = client.get(
        "/v1/protected",
        headers={"x-api-key": settings.api_key},
    )
    assert response.status_code == 200
    assert "message" in response.json()


def test_protected_fails_without_key(client: TestClient):
    response = client.get("/v1/protected")
    assert response.status_code == 403
