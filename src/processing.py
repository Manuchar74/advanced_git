from typing import Union


def filter_by_state(
    input_list: list[dict[str, Union[int, str]]], state="EXECUTED"
) -> list[dict[str, Union[int, str]]]:
    """принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ state
    соответствует указанному значению."""
    new_list = []
    for item in input_list:
        if "state" in item:
            if item.get("state") == state:
                new_list.append(item)
            else:
                continue
        else:
            continue

    return new_list


input_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


print(filter_by_state(input_list, state="CANCELED"))


def sort_by_date(
    list_to_sort: list[dict[str, Union[int, str]]], ascending: bool = True
) -> list[dict[str, Union[int, str]]]:
    """принимает список словарей и необязательный параметр, задающий порядок
    сортировки (по умолчанию — убывание). Функция должна возвращать новый список,
    отсортированный по дате (date)."""

    sorted_products = sorted(
        list_to_sort, key=lambda d: d.get("date", 0), reverse=bool(ascending)
    )

    return sorted_products


list_to_sort = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


print(sort_by_date(list_to_sort))
