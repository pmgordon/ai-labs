""""Tests for the main module"""
# pylint: disable=no-self-use
# pylint: disable=too-few-public-methods

from labs.main import main

class TestMain():
    """Tests for the main class"""

    def test_boilerplate(self):
        """Test pytest"""
        assert main() == 1
