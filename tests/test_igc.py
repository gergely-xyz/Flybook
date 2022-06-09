from flybook.igc import Igc
import datetime
import glob

def test_igc_from_file():
    # igc = Igc("tests/res/2022-02-12-XCT-GHO-01.igc")
    for igcfile in glob.glob("tests/res/*.igc"):
        igc = Igc(igcfile)
        flight_start = datetime.datetime.combine(igc.date, igc.records[0].time)
        flight_end = datetime.datetime.combine(igc.date, igc.records[-1].time)

        assert flight_end > flight_start

        flight_time = flight_end-flight_start