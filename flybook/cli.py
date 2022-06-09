import flybook as fb
import logging
import typer

APP = typer.Typer(name="cli", help="Command line interface")
LOG = logging.getLogger(__name__)

@APP.command(help="Placeholder")
def test():
    LOG.debug("CLI started")
    