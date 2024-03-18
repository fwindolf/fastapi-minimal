import os

import pytest
from fastapi.testclient import TestClient
from pydantic_settings import BaseSettings
from pytest_mock import MockerFixture


@pytest.fixture(autouse=True)
def env_setup(mocker: MockerFixture):
    envs = {
        "API_KEY": "test1234",
    }
    mocker.patch.dict(os.environ, envs)


@pytest.fixture
def client(env_setup) -> TestClient:
    from api import app

    return TestClient(app)


@pytest.fixture
def settings(env_setup) -> BaseSettings:
    from api.settings import settings

    return settings
