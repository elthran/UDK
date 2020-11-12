import os
import sys

import pytest
import expects

from app.main import app


# Inject all expect helpers as builtins
for key in expects.__all__:
    if key in __builtins__:
        print('Overlap with builtin on', key)
        continue

    __builtins__[key] = getattr(expects, key)


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
