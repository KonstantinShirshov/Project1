from typing import Any, Dict, List


def filter_by_state(dictionary_inform: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Функция, которая принимает список словарей и опционально значение ключа
    и возвращает новый список словарей
    """
    list_state = []
    for key in dictionary_inform:
        if key.get("state") == state:
            list_state.append(key)
    return list_state


def sort_by_date(dictionary_inform: list[dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция, которая сортирует список по дате и возвращает новый список"""
    sorted_list = sorted(dictionary_inform, key=lambda x: x['date'], reverse=True)
    return sorted_list
