import click

@click.command()
def print_conf():
    """Print the configuration.
    """
    from ospm.commands.print_config import print_config
    click.echo("Printing the configuration from the CLI.")
    print_config()
