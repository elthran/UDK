import logging

import pytest

from app.main import app

asyncio_logger = logging.getLogger("asyncio")
asyncio_logger.setLevel(logging.INFO)  # Silence useless asyncio debug messages.
faker_logger = logging.getLogger("faker")
faker_logger.setLevel(logging.INFO)  # Quiet faker locale messages down in tests.


@pytest.fixture
def client():
    with app.app_context():
        with app.test_client() as client:
            yield client


@pytest.fixture
def login(client):
    def _login(username):
        return client.post(
            "/api/authentication/login",
            json=dict(username=username),
            follow_redirects=True,
        ).get_json()

    return _login
