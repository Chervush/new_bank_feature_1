from datetime import datetime

from Data.test_data import list_of_dates



def filter_by_state(list_of_dates: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция принимает список словарей и возвращает новый список словарей, содержащий только те словари,
    у которых ключ state
    соответствует указанному значению: "EXECUTED" или "CANCELED"."""

    filtered = []
    for entry in list_of_dates:
        if entry.get("state") == state:
            filtered.append(entry)
    return filtered


def sort_by_date(list_of_dates: list[dict], is_reversed: bool = True) -> list[dict]:
    """'Функция принимает список словарей и необязательный параметр is_reversed, задающий порядок сортировки
    (по умолчанию — убывание).
    Функция возвращает новый список словарей, отсортированный по дате"""

    sorted_list = sorted(
        list_of_dates,
        key=lambda entry: datetime.fromisoformat(entry["date"]),
        reverse=is_reversed
    )
    return sorted_list

print(sort_by_date([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30 02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14'},
]))