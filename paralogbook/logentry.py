from dataclasses import dataclass
from datetime import date, timedelta

@dataclass
class LogEntry():
    date: date
    pilot: str
    glider: str
    max_altitude: int
    air_time: timedelta
    distance: float
    site: str

    @classmethod
    def from_igc_file(cls, filename):
        raise NotImplementedError()

    def save_to_file(self, filename):
        raise NotImplementedError()

    @classmethod
    def load_from_file(cls, filename):
        raise NotImplementedError()
