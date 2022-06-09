import flybook as fb
import typer

import logging
import os

def main(debug: bool = typer.Option(False, "--debug", "-d", help="Print debug messages to stdout")):
    if debug:
        fb.Logger.stream_handler.setLevel(logging.DEBUG)
        LOG.debug("Debug mode enabled")

LOG = logging.getLogger(__name__)
APP = typer.Typer(callback=main)
# APP.add_typer(fb.gui.APP)
APP.add_typer(fb.cli.APP)


if __name__ == "__main__":
    APP()

