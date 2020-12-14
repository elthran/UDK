import logging

import pytest

from app.main import app

asyncio_logger = logging.getLogger("asyncio")
asyncio_logger.setLevel(logging.INFO)  # Silence useless asyncio debug messages.
faker_logger = logging.getLogger("faker")
faker_logger.setLevel(logging.INFO)  # Quiet faker locale messages down in tests.


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
