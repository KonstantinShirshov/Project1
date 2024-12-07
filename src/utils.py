import json
from json import JSONDecodeError


def get_operations_data(path: str) -> list:
    try:
        with open(path, encoding='utf-8') as f:
            try:
                data_json = json.load(f)
            except JSONDecodeError:
                print('Ошибка декодирования файла')
                return []
        return data_json
    except FileNotFoundError:
        print('Файл не найден')
        return []


if __name__ == '__main__':
    path = '../data/operations.json'
    print(get_operations_data(path))
