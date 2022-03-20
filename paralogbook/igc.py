import datetime
from dataclasses import dataclass

@dataclass
class BRecord:
    time: datetime.time
    latitude: float
    longitude: float
    validity: str
    preassure_altitude: int
    gps_altitude: int

class Igc:
    pilot: str
    site: str    
    glider: str
    date: datetime.date
    flight_num: int
    records: list[BRecord] = []
    flight_time: datetime.timedelta

    def __init__(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                self.process_line(line)

        flight_start = datetime.datetime.combine(self.date, self.records[0].time)
        flight_end = datetime.datetime.combine(self.date, self.records[-1].time)
        self.flight_time = flight_end-flight_start

    def __str__(self):
        igc_string = f"Pilot: {self.pilot}\n"
        igc_string += f"Site: {self.site}\n"
        igc_string += f"Site: {self.glider}\n"
        igc_string += f"Date: {self.date}\n"
        igc_string += f"Flight: {self.flight_num}\n"
        igc_string += f"Length: {self.flight_time}\n"

        return igc_string

    @staticmethod
    def decode_date(date_str):

        if len(date_str) != 6:
            raise ValueError('Date string does not have correct length')
        elif date_str == '000000':
            return None

        dd = int(date_str[0:2])
        mm = int(date_str[2:4])
        yy = int(date_str[4:6])

        current_year_yyyy = datetime.date.today().year
        current_year_yy = current_year_yyyy % 100
        current_century = current_year_yyyy - current_year_yy
        yyyy = current_century + yy if yy <= current_year_yy else current_century - 100 + yy

        return datetime.date(yyyy, mm, dd)

    @staticmethod
    def decode_time(time_str):

        if len(time_str) != 6:
            raise ValueError('Time string does not have correct size')

        h = int(time_str[0:2])
        m = int(time_str[2:4])
        s = int(time_str[4:6])

        return datetime.time(h, m, s)

    @staticmethod
    def decode_latitude(lat_string):

        d = int(lat_string[0:2])
        m = float(lat_string[2:7]) / 1000
        ordinal = lat_string[7]

        latitude = d + m / 60.

        if not (0. <= latitude <= 90):
            raise ValueError('Latitude format is invalid')

        if ordinal == 'S':
            latitude = -latitude

        return latitude

    @staticmethod
    def decode_longitude(lon_string):

        d = float(lon_string[0:3])
        m = float(lon_string[3:8]) / 1000
        ordinal = lon_string[8]

        longitude = d + m / 60.

        if not (0. <= longitude <= 180):
            raise ValueError('Longitude format is invalid')

        if ordinal == 'W':
            longitude = -longitude

        return longitude

    def process_line(self, line):
        if "HFPLTPILOTINCHARGE" in line:
            self.pilot = line.split(':')[1].strip()
        if "HOSITSite" in line:
            self.site = line.split(':')[1].strip()
        if "HFGTYGLIDERTYPE" in line:
            self.glider = line.split(':')[1].strip()
        if "HFDTEDATE" in line:
            data = line.split(':')[1].strip().split(',')
            date_str = data[0]
            self.date = datetime.date(int(f"20{date_str[4:6]}"), int(date_str[2:4]), int(date_str[0:2]))
            self.flight_num = int(data[1])
        if line[0] == 'B':
            b_record = BRecord(
                Igc.decode_time(line[1:7]),
                Igc.decode_latitude(line[7:15]),
                Igc.decode_longitude(line[15:24]),
                line[24],
                int(line[25:30]),
                int(line[30:35]),
                )
            self.records.append(b_record)

    
if __name__ == "__main__":
    i = Igc("/home/gery/Documents/Tracklogs/2022-02-12-XCT-GHO-01.igc")
    print(i)

    # for c, r in enumerate(i.records):
    #     print(c, r)
