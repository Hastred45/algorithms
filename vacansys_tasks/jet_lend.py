from itertools import groupby
from typing import Any, List


def remove_duplicates_1(lst: List[dict[str, Any]]) -> List[dict[str, Any]]:
    unique = set()
    result = []
    for item in lst:
        # преобразуем dict-объект в неизменяемый хэшабельный тип данных tuple
        # для возможности добавления в Set
        item_hashable = tuple(item.items())
        if item_hashable not in unique:
            unique.add(item_hashable)
            result.append(item)
    return result


def remove_duplicates_2(lst: List[dict[str, Any]]) -> List[dict[str, Any]]:
    # используем генератор списков для создания нового списка
    # проверяем уникальность элементов на основе сравнения их ключей
    return [dict(t) for t in set([tuple(d.items()) for d in lst])]


def remove_duplicates_3(lst: List[dict[str, Any]]) -> List[dict[str, Any]]:
    # сортируем список, чтобы группировка работала корректно
    sorted_lst = sorted(lst, key=lambda d: tuple(d.items()))
    # используем groupby для группировки по ключу, кортежу из элементов словаря
    # создаем новый список словарей из первого элемента каждой группы
    return [
        next(g) for k, g in groupby(sorted_lst, key=lambda d: tuple(d.items()))
    ]


if __name__ == "__main__":

    lst = [{"key1": "value1"},
           {"k1": "v1", "k2": "v2", "k3": "v3"},
           {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]

    print(f"Результат работы 1 функции: {remove_duplicates_1(lst)}\n"
          f"Результат работы 2 функции: {remove_duplicates_2(lst)}\n"
          f"Результат работы 3 функции: {remove_duplicates_3(lst)}")
