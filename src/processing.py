from typing import List, Dict, Any


def filter_by_state(dictionary_inform: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Функция, которая принимает список словарей и опционально значение ключа
    и возвращает новый список словарей
    """
    list_state = []
    for key in dictionary_inform:
        if key.get('state') == state:
            list_state.append(key)
    return list_state


def sort_by_date(dictionary_inform: list[dict[str, Any]], reverse = True) -> list[dict[str, Any]]:
    """Функция, которая сортирует список по дате и возвращает новый список"""
    sorted_list = sorted(dictionary_inform, key=lambda x: x['date'], reverse = True)
    return sorted_list


dictionary_inform = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


print(filter_by_state(dictionary_inform))
print(sort_by_date(dictionary_inform))
