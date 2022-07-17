import configparser
import logging
import os
from pathlib import Path
from typing import Optional

import typer

import flybook as fb

APP = typer.Typer(name="config", help="Configuration")
LOG = logging.getLogger(__name__)
CONFIG = configparser.ConfigParser()
DEFAULT_LOGDIR = "~/Documents/Tracklogs"

if not os.path.isfile(fb.CONF_FILE):
    CONFIG["Settings"] = {}
    CONFIG["Settings"]["logdir"] = os.path.expanduser(DEFAULT_LOGDIR)
    CONFIG["Settings"]["sort"] = "date"

    CONFIG["Show"] = {}
    CONFIG["Show"]["Stars"] = "yes"
    CONFIG["Show"]["Pilot"] = "no"
    CONFIG["Show"]["Date"] = "yes"
    CONFIG["Show"]["Glider"] = "yes"
    CONFIG["Show"]["Site"] = "yes"

    CONFIG["Group"] = {}
    CONFIG["Group"]["Pilot"] = "yes"
    CONFIG["Group"]["Year"] = "no"
    CONFIG["Group"]["Glider"] = "no"
    CONFIG["Group"]["Country"] = "no"

    with open(fb.CONF_FILE, 'w') as configfile:
        CONFIG.write(configfile)

CONFIG.read(fb.CONF_FILE)

@APP.command()
def logdir(path: Path = typer.Argument(DEFAULT_LOGDIR, help="Path to the folder where .igc files are stored")):
    logdir = os.path.expanduser(path)
    if logdir != CONFIG["Settings"].get("logdir", DEFAULT_LOGDIR):
        CONFIG["Settings"]["logdir"] = str(logdir)
        with open(fb.CONF_FILE, 'w') as configfile:
            CONFIG.write(configfile)
    else:
        print(logdir)
