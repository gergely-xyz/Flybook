import paralogbook as plb
from datetime import date
from datetime import timedelta

def test_logentry_from_file():
    entry = plb.logentry.LogEntry.from_igc_file("tests/res/2022-02-12-XCT-GHO-01.igc")
    print(entry)
    assert entry.pilot == "Gergely Horváth"
    assert entry.site.name == "?"
    assert entry.site.coutry == "Spain"
    assert entry.site.coutry_code == "ES"
    assert entry.site.nearest_city == "Algodonales"
    assert entry.date == date(2022, 2, 12)
    assert entry.flight_number == 1
    assert entry.glider == "NOVA Ion 3"
    assert entry.flight_time == timedelta(seconds=546)