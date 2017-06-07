"""Module for testing weekday function."""
import weekday


def test_simple():
    excepted = 2
    acctualy = weekday.weekday(2017, 6, 7)
    assert excepted == acctualy


def test_wrong_month():
    excepted = None
    acctualy = weekday.weekday(2017, 13, 7)
    assert excepted == acctualy


def test_wrong_day():
    excepted = None
    acctualy = weekday.weekday(2017, 6, 31)
    assert excepted == acctualy


def test_feb():
    excepted = 0
    acctualy = weekday.weekday(2016, 2, 28)
    assert excepted == acctualy


def test_feb2():
    excepted = None
    acctualy = weekday.weekday(2100, 2, 29)
    assert excepted == acctualy


def test_feb3():
    excepted = 1
    acctualy = weekday.weekday(2000, 2, 29)
    assert excepted == acctualy


def test_first_year():
    excepted = 2
    acctualy = weekday.weekday(1, 6, 5)
    assert excepted == acctualy


def test_far_date():
    excepted = 1
    acctualy = weekday.weekday(2891, 6, 5)
    assert excepted == acctualy


def test_middleage():
    excepted = 2
    acctualy = weekday.weekday(1400, 4, 14)
    assert excepted == acctualy


def test_wrong_type():
    excepted = None
    acctualy = weekday.weekday("1400", 4, 14)
    assert excepted == acctualy
