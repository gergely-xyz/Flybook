import paralogbook as plb

def test_logbook_from_folder():
    lb = plb.logbook.LogBook.from_igc_folder("tests/res")
    print(lb)
