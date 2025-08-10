import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import list_of_dates, list_of_dates_no_state_entry, list_of_dates_same_date, list_of_dates_different_date_formats


def test_filter_by_state_executed(list_of_dates):
    assert filter_by_state(list_of_dates, 'EXECUTED' ) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


def test_filter_by_state_canceled(list_of_dates):
    assert filter_by_state(list_of_dates, 'CANCELED') == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

def test_filter_by_state_not_defined(list_of_dates):
    assert filter_by_state(list_of_dates) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
        ]

def test_filter_by_state_no_state_entry(list_of_dates_no_state_entry):
    assert filter_by_state(list_of_dates_no_state_entry) == []


list_of_dates = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]

@pytest.mark.parametrize ('list_of_dates, state, expected',[
    (list_of_dates,'EXECUTED', [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]),
    (list_of_dates, 'CANCELED', [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ])
])
def test_filter_by_state_different_states(list_of_dates, state, expected):
    assert filter_by_state(list_of_dates, state) == expected



sorted_by_date_reversed = [
                                  {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
sorted_by_date = [
                                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                                  {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]



@pytest.mark.parametrize ('list_of_dates, is_reversed, expected',[
                              (list_of_dates, True, sorted_by_date_reversed
                               ),
                              (list_of_dates, False, sorted_by_date
                               ),
                          ])
def test_sort_by_date(list_of_dates, is_reversed, expected):
    assert sort_by_date(list_of_dates, is_reversed) == expected


def test_sort_by_date_same_date(list_of_dates_same_date):
    assert sort_by_date(list_of_dates_same_date) == list_of_dates_same_date

def test_list_of_dates_different_date_formats(list_of_dates_different_date_formats):
    assert sort_by_date(list_of_dates_different_date_formats) == [
                                                            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29'},
                                                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14'},
                                                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30 02:08:58.425572'}]
    assert sort_by_date(list_of_dates_different_date_formats, False) == [
                                                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30 02:08:58.425572'},
                                                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14'},
                                                            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29'}]
