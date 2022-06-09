import flybook as fb

def test_logbook_from_folder():
    lb = fb.logbook.LogBook.from_igc_folder("tests/res")

