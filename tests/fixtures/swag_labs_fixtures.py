"""Generate a unique test session ID."""
import pytest

from uuid import uuid4
from tests.consts import PROJECT_DIR

@pytest.fixture(scope="session")
def test_session_id() -> str:
    """Generate a unique test session ID."""
    test_session_id = str(PROJECT_DIR.name) + str(uuid4())[:6]
    return test_session_id
