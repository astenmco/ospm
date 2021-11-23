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
from cli import print_conf
from cli import project

# logging integration to click setup
click_log.basic_config(logging.getLogger())


@click.group()  # Main CLI entrypoint for the following subcommands
@click_log.simple_verbosity_option(logging.getLogger()) # Add a verbosity option and binds it to the logs handler
@click.option('-c', '--config-file',
              type=click.Path(),
              help="Specify a configuration file.")
@click.option('-d', '--dry-run',
              default=False,
              help="Do not actually run the command, simply print what the actual command would do instead.")
def cli(config_file, dry_run):
    """CLI for the OpenShift Project Manager
    """
    ospm.Conf().set_configuration_file(config_file)

cli.add_command(print_conf.print_conf)
cli.add_command(project.project)