from PySide6.QtCore import QAbstractTableModel

class LogBook(QAbstractTableModel):
    def __init__(self, flightlogs, parent=None):
        super().__init__(parent)
        self.records = flightlogs
        self.headers = ["Date", "Pilot", "Glider"]

    def columnCount(self, parent):
        """ Return the number of columns to be displayed. """
        return len(self.headers)

    def rowCount(self, parent):
        """ Return the number of rows to be displayed. """
        return len(self.records)

