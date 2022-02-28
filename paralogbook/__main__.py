import paralogbook as plb
import typer

import logging

def main(debug: bool = typer.Option(False, "--debug", "-d", help="Print debug messages to stdout")):
    if debug:
        plb.Logger.stream_handler.setLevel(logging.DEBUG)

LOG = logging.getLogger(__name__)
APP = typer.Typer(callback=main)
APP.add_typer(plb.gui.APP)

if __name__ == "__main__":
    APP()

