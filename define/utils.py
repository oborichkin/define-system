import random
import math

from typing import Generator, List, Generic, Iterable, Callable, Tuple
from collections import defaultdict


def kw(x: tuple, y: tuple) -> int:
    """Возвращает число атрибутов отличаюшихся между x и y по значению

    Args:
        x (tuple): Первый элемент
        y (tuple): Второй элемент

    Returns:
        int: число отличающихся атриьбутов
    """
    assert len(x) == len(y)
    count = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            count += 1
    return count


def mw(attr: int, d_plus: tuple, Q_j: List[tuple]) -> int:
    """Возвращает число контрпримеров в Q_j к d_plus по атрибуту attr

    Args:
        attr (int): Индекс атрибута
        d_plus (tuple): Положительный элемент
        Q_j (List[tuple]): Множество элементов для сравнения

    Returns:
        int: Число контрпримеров
    """
    count = 0
    for d_minus in Q_j:
        if d_plus[attr] != d_minus[attr]:
            count += 1
    return count


def mw_advanced(attr: int, d_plus: tuple, Q_j: List[tuple]) -> Tuple[int, int]:
    count = 0
    values = set()
    for d_minus in Q_j:
        if d_plus[attr] != d_minus[attr]:
            count += 1
            values.add(d_minus[attr])
    return (count, len(values))


def find_max(iterable: Iterable, iter_method: Callable, key: Callable = None) -> int:
    _max = None
    return_value = None
    for x in iter_method(iterable):
        value = x if not key else key(x)
        if not _max or value > _max:
            return_value = x
            _max = value
    return return_value


def find_min(iterable: Iterable, iter_method: Callable, key: Callable = None) -> int:
    _min = None
    return_value = None
    for x in iter_method(iterable):
        value = x if not key else key(x)
        if not _min or value < _min:
            return_value = x
            _min = value
    return return_value


def distinguishing(x: tuple, y: tuple) -> Generator[int, None, None]:
    """Генератор возвращающий индексы отличающихся атрибутов между x и y

    Args:
        x (tuple): Первый элемент
        y (tuple): Второй элемент

    Yields:
        Generator[int]: Генератор с индексами
    """
    assert len(x) == len(y)
    for i in range(len(x)):
        if x[i] == y[i]:
            continue
        yield i


def dict_from_csv(filename: str, sep: str = ",") -> dict:
    """Чтение файла с исходными данными.
    Значение класса указывается в полследнем столбце.

    Args:
        filename (str): Имя файла
        sep (str, optional): Разделитель значений. Defaults to ",".

    Returns:
        dict: словарь с ключами - классами, значениями - элементами класса
    """
    res_list = list_from_csv(filename, sep)
    res = defaultdict(list)
    for x in res_list:
        res[x[-1]].append(x[:-1])
    return res


def list_from_csv(filename: str, sep: str = ",") -> list:
    """Чтение csv файла с данными

    Args:
        filename (str): Имя файла
        sep (str, optional): Разделитель значений. Defaults to ",".

    Returns:
        list: Список кортежей
    """
    res = []
    with open(filename, "r") as f:
        for line in f.readlines():
            res.append(tuple(line.strip().split(sep)))
    return res


def randomly(lst: List) -> Generator:
    """Генератор для рандомной итерации по списку

    Args:
        lst (List): Список

    Yields:
        Generator: Элементы списка в случайном порядке
    """
    for value in sorted(lst, key=lambda _: random.random()):
        yield value
