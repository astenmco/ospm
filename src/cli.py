""" CLI entrypoint.
    Not to be used in an "import context".
"""

# Low level imports
import logging
import click_log # logging integration to click

# High level imports
import click # Command Line Interface Creation Kit

# Local imports
import ospm

# logging integration to click setup
click_log.basic_config(logging.getLogger())


@click.group()  # Main CLI entrypoint for the following subcommands
@click_log.simple_verbosity_option(logging.getLogger()) # Add a verbosity option and binds it to the logs handler
@click.option('-c', '--config-file',
              type=click.Path(),
              help="Specify a configuration file.")
def cli(config_file):
    """CLI for the OpenShift Project Manager
    """
    ospm.Conf().set_configuration_file(config_file)

@cli.command()
def print_conf():
    """Print the configuration.
    """
    from ospm.commands import print_config
    print_config()

@cli.group()
def init():
    """Initialize a new project working environment.
    """
    pass

@init.command()
def bare():
    """Initializing a bare project.
    """
    click.echo('Initializing a bare project')

@init.command()
def existing():
    """Initializing a project from an existing one.
    """
    click.echo('Initializing a project from existing.')

@cli.command()
def deploy():
    """Deploy a project on a cluster.
    """
    click.echo('Deploying a project')
