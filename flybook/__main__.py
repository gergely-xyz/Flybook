import datetime
import logging
import os
from glob import glob
from importlib.metadata import metadata, version

import typer
from rich.console import Console
from rich.table import Column, Table

import flybook as fb

LOG = logging.getLogger(__name__)
APP = typer.Typer()
APP.add_typer(fb.config.APP)
# APP.add_typer(fb.gui.APP)
# APP.add_typer(fb.cli.APP)

@APP.callback() # invoke_without_command=True
def main(verbose: bool = typer.Option(False, "--verbose", "-v", help="Print debug messages to stdout")):
    if verbose:
        fb.Logger.stream_handler.setLevel(logging.DEBUG)
        LOG.debug("Verbose mode enabled")

@APP.command(name="version", help="Print the version and exit")
def fbversion():
    print(metadata('flybook')["Name"], "version", version('flybook'))
    exit()

def starred(stat_string):
    return f":star: [yellow][bold]{stat_string}[/bold][/yellow]"

@APP.command(help="Show the logs stored in Flybook")
def show():
    lb = fb.logbook.LogBook.from_igc_folder(fb.config.CONFIG["Settings"]["logdir"])

    table = Table(show_header=True, header_style="bold blue", title=f"Pilot: {lb.records[0].pilot}", show_footer=True)
    table.add_column("#", style="dim", justify="right")
    table.add_column("Date & count", style="dim")
    table.add_column("Takeoff", style="dim", justify="center")
    table.add_column("Landing", style="dim", justify="center")
    table.add_column("Glider")
    table.add_column("Max GPS alt. (m)", justify="right")
    
    airtime = Column(header="Time", justify="right")
    table.columns.append(airtime)

    table.add_column("Site")

    airtime_sum = datetime.timedelta()
    for i, r in enumerate(lb.records):
        date_str = f"{r.date} #{r.flight_number}"
        takeoff_str = f"{r.takeoff_time:%H:%M}"
        landing_str = f"{r.landing_time:%H:%M}"
        altitude_str = starred(r.max_altitude) if r is lb.highest_flight else str(r.max_altitude)
        airtime_str = starred(r.airtime) if r is lb.longest_flight else str(r.airtime)
        sire_str = f"{r.site.coutry} - {r.site.name if r.site.name != '?' else r.site.nearest_city} "
        table.add_row(str(i+1), date_str, takeoff_str, landing_str, r.glider, altitude_str, airtime_str, sire_str)

        airtime_sum += r.airtime

    airtime.footer = f"Σ {airtime_sum}"
    
    console = Console()
    console.print(table)

if __name__ == "__main__":
    APP()
