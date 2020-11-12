import os
import sys

import pytest

# hack path
sys.path.insert(0, os.getcwd())
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        print("client", client)
        # with app.app_context():
        #     init_db()
        yield client
