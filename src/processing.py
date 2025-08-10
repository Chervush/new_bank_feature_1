from datetime import datetime


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

    sorted_list = sorted(list_of_dates, key=lambda entry: datetime.fromisoformat(entry["date"]), reverse=is_reversed)
    return sorted_list
