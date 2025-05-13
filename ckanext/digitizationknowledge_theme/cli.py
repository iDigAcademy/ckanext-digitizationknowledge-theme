import click


@click.group(short_help="digitizationknowledge_theme CLI.")
def digitizationknowledge_theme():
    """digitizationknowledge_theme CLI.
    """
    pass


@digitizationknowledge_theme.command()
@click.argument("name", default="digitizationknowledge_theme")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [digitizationknowledge_theme]
