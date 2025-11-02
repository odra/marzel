import pytest
from click.testing import CliRunner


@pytest.fixture
def clitest():
    return CliRunner()
