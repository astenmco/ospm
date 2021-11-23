import click

@click.command()
def clone():
    """Clone a project.
    """
    click.echo('Cloning a project from the CLI.')