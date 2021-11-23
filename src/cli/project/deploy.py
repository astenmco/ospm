import click

@click.command()
def deploy():
    """Deploy a project on a cluster.
    """
    click.echo('Deploying a project from the CLI.')