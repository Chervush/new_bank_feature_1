# тестовый словарь для проверки
list_of_dates = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(list_of_dates: list, state: str = 'EXECUTED') -> list:

    '''Функция принимает список словарей и возвращает новый список словарей, содержащий только те словари,
    у которых ключ state
    соответствует указанному значению.'''

    filtered = []
    for entry in list_of_dates:
        if entry.get('state') == state:
            filtered.append(entry)
    return filtered


def sort_by_date(list_of_dates: list, reversed: bool = True) -> list:
    ''''Функция принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание).
    Функция возвращает новый список словарей, отсортированный по дате'''

    sorted_list = sorted(list_of_dates, key=lambda entry: (entry['date'])[-6:], reverse=reversed)
    return sorted_list

# Проверка работы функций


print(filter_by_state(list_of_dates))
print(sort_by_date(list_of_dates))
