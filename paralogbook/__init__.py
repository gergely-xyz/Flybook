import logging
import os

import appdirs

import paralogbook.gui
import paralogbook.logbook

__author__ = "gergely-xyz"

DIRS = appdirs.AppDirs(__name__, __author__)
CONF_DIR = DIRS.user_config_dir
CONF_FILE = os.path.join(CONF_DIR, "config.ini")
LOG_DIR = DIRS.user_log_dir
LOG_FILE = os.path.join(LOG_DIR, "paralogbook.log")
LOG_FORMAT = "%(asctime)s:%(levelname)s:%(name)s:%(message)s"
DATA_DIR = DIRS.user_data_dir
CACHE_DIR = DIRS.user_cache_dir

# Create a directories if neccessary
os.makedirs(CONF_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(CACHE_DIR, exist_ok=True)


class Logger(logging.getLoggerClass()):

    formatter = logging.Formatter(LOG_FORMAT)
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)
    stream_handler.setFormatter(formatter)

    def __init__(self, name):
        super().__init__(name)
        self.setLevel(logging.DEBUG)
        self.addHandler(Logger.file_handler)
        self.addHandler(Logger.stream_handler)


logging.setLoggerClass(Logger)
