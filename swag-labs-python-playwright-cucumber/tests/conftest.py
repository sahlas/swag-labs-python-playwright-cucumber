"""Path requirements."""
import sys
from pathlib import Path

THIS_DIR = Path(__file__).parent
TESTS_DIR_PARENT = (THIS_DIR / "..").resolve()

# Add the parent directory to the Python path
sys.path.insert(0, str(TESTS_DIR_PARENT))

pytest_plugins = ["tests.fixtures.example_fixture"]
