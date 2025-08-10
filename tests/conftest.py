import pytest


@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"
def test_get_date(date):
    assert get_date(date) == '11.03.2024'


@pytest.fixture
def wrong_number():
    return '993002!_hey_man'