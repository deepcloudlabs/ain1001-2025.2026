import pytest


def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


leap_years = [2000, 2400, 2004, 2800, 2104,2204]
not_leap_years = [2001, 2002, 2003, 3000, 2005, 2100, 2200, 2300, 2500, 2600]


@pytest.mark.parametrize("year", leap_years)
def test_leap_years(year):
    assert is_leap_year(year) == True


@pytest.mark.parametrize("year", not_leap_years)
def test_not_leap_years(year):
    assert is_leap_year(year) == False
