import click

from cli.project import clone, deploy, init

@click.group()
@click.argument('project-name',
                type=click.STRING)
def project(project_name):
    """Work with a project.
    """
    pass

project.add_command(init.init)
project.add_command(clone.clone)
project.add_command(deploy.deploy)
