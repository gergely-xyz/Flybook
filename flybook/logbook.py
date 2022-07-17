from flybook.logentry import LogEntry
from glob import glob
import os

class LogBook():
    def __init__(self, logs: list[LogEntry]):
        self.records = logs
    
    def __str__(self):
        logbook_string = f"Logbook with {len(self.records)} entries.\n"
        # for r in self.records:
        #     logbook_string += str(r) + '\n'
        
        return logbook_string

    @classmethod
    def from_igc_folder(cls, folder_path):
        logs = []
        for igc_file in glob(os.path.join(folder_path, "*.igc")):
            logs.append(LogEntry.from_igc_file(igc_file))
                
        logs.sort(key=lambda x: (x.date, x.flight_number))
        return cls(logs)

    @property
    def highest_flight(self):
        return max(self.records, key=lambda r: r.max_altitude)

    @property
    def longest_flight(self):
        return max(self.records, key=lambda r: r.airtime)

