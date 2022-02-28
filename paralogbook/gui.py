""" Submodule of the main graphical user interface """
from PySide6 import QtCore, QtGui, QtWidgets, QtUiTools
import typer

import logging
import sys

import paralogbook as plb

LOG = logging.getLogger(__name__)
APP = typer.Typer(name="gui", help="Graphical user interface")
MAIN_WIN_BASE, MAIN_WIN_UI = QtUiTools.loadUiType("res/main.ui")

class Window(MAIN_WIN_BASE, MAIN_WIN_UI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableView.setModel(plb.logbook.LogBook([]))

@APP.command(help="Start the GUI")
def start():
    # translator = QtCore.QTranslator()
    # translator.load('res/hu_HU')
    app = QtWidgets.QApplication(sys.argv)
    # app.installTranslator(translator)
    window = Window()
    window.show()
    sys.exit(app.exec())

