from typing import List, Dict, Any


def filter_by_state(dictionary_inform: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[srt, Any]]:
    """
    Функция, которая принимает список словарей и опционально значение ключа
    и возвращает новый список словарей
    """
    list_state = []
    for key in dictionary_inform:
        if key.get('state') == state:
            list_state.append(key)
            return list_state


def sort_by_date(date_list: list, reverse: bool = True) -> list[dict[str, Any]]:
    """Функция, которая сортирует список по дате и возвращает новый список"""
    sorted_list = sorted(date_list, key = lambda date_dict: date_dict.get('date'), reverse = True)


print(filter_by_state(dictionary_inform))
print(sort_by_date(date_list))