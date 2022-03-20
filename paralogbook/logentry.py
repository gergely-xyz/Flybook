import paralogbook as plb

import reverse_geocode

from dataclasses import dataclass
import datetime 

@dataclass
class Site:
    name: str
    coutry: str
    coutry_code: str
    nearest_city: str

@dataclass
class LogEntry():
    pilot: str
    site: Site
    glider: str
    date: datetime.date
    flight_number: int

    flight_time: datetime.timedelta
    # max_altitude: int

    @classmethod
    def from_igc_file(cls, filename):
        igc = plb.igc.Igc(filename)
        

        flight_start = datetime.datetime.combine(igc.date, igc.records[0].time)
        flight_end = datetime.datetime.combine(igc.date, igc.records[-1].time)
        flight_time = flight_end-flight_start

        start = igc.records[0]
        start_cords = start.latitude, start.longitude
        location = reverse_geocode.get(start_cords)
        site = Site(igc.site, location["country"], location["country_code"], location["city"])

        return cls(igc.pilot, site, igc.glider, igc.date, igc.flight_number, flight_time)

    def save_to_file(self, filename):
        raise NotImplementedError()

    @classmethod
    def load_from_file(cls, filename):
        raise NotImplementedError()

if __name__ == "__main__":
    le = LogEntry.from_igc_file("/home/gery/Documents/Tracklogs/2022-02-12-XCT-GHO-01.igc")
    print(le)
