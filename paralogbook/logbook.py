from PySide6.QtCore import QAbstractTableModel
from paralogbook.logentry import LogEntry
from glob import glob
import os

class LogBook():
    def __init__(self, logs: list[LogEntry]):
        self.records = logs
    
    @classmethod
    def from_igc_folder(cls, folder_path):
        logs = []
        for igc_file in glob(os.path.join(folder_path, "*.igc")):
            logs.append(LogEntry.from_igc_file(igc_file))
                
        return cls(logs)

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

if __name__ == "__main__":
    lb = LogBook.from_igc_folder("/home/gery/Documents/Tracklogs")
    for record in lb.records:
        print(record.date)
