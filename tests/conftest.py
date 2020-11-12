import os
import sys

import pytest

from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        print("client", client)
        # with app.app_context():
        #     init_db()
        yield client
