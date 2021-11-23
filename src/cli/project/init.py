import click

@click.command()
def init():
    """Initialize a new project workspace.
    """
    click.echo('Initializing a project from the CLI.')