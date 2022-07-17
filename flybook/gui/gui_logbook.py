from PySide6.QtCore import QAbstractTableModel

class LogBookTable(LogBook, QAbstractTableModel):
    def __init__(self, flightlogs, parent=None):
        LogBook.__init__(self, flightlogs)
        QAbstractTableModel.__init__(self, parent)

        self.headers = ["Date", "Pilot", "Glider"]

    def columnCount(self, parent):
        """ Return the number of columns to be displayed. """
        return len(self.headers)

    def rowCount(self, parent):
        """ Return the number of rows to be displayed. """
        return len(self.records)
