import logging

import pytest

from app.main import app

logger = logging.getLogger("faker")
logger.setLevel(logging.INFO)  # Quiet faker locale messages down in tests.


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
