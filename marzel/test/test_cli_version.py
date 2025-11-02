from marzel import __version__ as _v
from marzel.cli import cli


def test_version(clitest):
    res = clitest.invoke(cli, ['version'])

    expected_rc = 0
    expected_output = [
        f'v{_v}',
        ''
    ]

    assert expected_rc == res.exit_code
    assert '\n'.join(expected_output) == res.output
