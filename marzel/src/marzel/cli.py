import click

from . import __version__ as _v

@click.group
def cli():
    """Marzel: the marshal of Bazel builds"""
    pass


@cli.command
def version():
    """Show program version"""
    click.echo(f'v{_v}')


def run():
    cli()
