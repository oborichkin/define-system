import copy

from collections import defaultdict
from typing import List, Generator

from .utils import kw, mw, distinguishing, find_max, find_min, randomly, mw_advanced


def poisk(d_plus: tuple, Q_j_orig: List[tuple], iter_method=list) -> set:
    """Реазлизация алгоритма POISK

    Args:
        d_plus (tuple): Положительный элемент
        Q_j_orig (List[tuple]): Класс для сравнения
        iter_method (Callable, optional): Метод перебора значений (какой то из list, reversed, randomly). Defaults to list.

    Returns:
        set: Минимальный набор тестов для d_plus и Q_j
    """
    t = set()
    Q_j = copy.deepcopy(Q_j_orig)
    if d_plus in Q_j:
        Q_j.remove(d_plus)
    _kw = {d_minus: kw(d_plus, d_minus) for d_minus in Q_j}
    _mw = {i: mw(i, d_plus, Q_j) for i in range(len(d_plus))}

    while Q_j:
        d_minus_selected = find_min(_kw, iter_method, _kw.get)
        diff_attr = {k: v for k, v in _mw.items() if k in distinguishing(d_plus, d_minus_selected)}
        attr_selected = find_max(diff_attr, iter_method, diff_attr.get)
        t.add(attr_selected)
        for_deletion = []
        for d_minus in Q_j:
            if attr_selected in distinguishing(d_plus, d_minus):
                for attr in distinguishing(d_plus, d_minus):
                    _mw[attr] -= 1
                for_deletion.append(d_minus)
        for d in for_deletion:
            Q_j.remove(d)
            _kw.pop(d)
    return t


def my_poisk(d_plus: tuple, Q_j_orig: List[tuple], mw_method=mw, mw_recalculate=False, iter_method=list) -> set:
    """Мой слегка видоизмененный алгоритм POISK

    Args:
        d_plus (tuple): Положительный элемент
        Q_j_orig (List[tuple]): Класс для сравнения
        mw_method (Callable, optional): Метод расчета mw (mw или mw_advanced). Defaults to mw.
        mw_recalculate (bool, optional): Нужно ли пересчитывать mw на каждом шаге. Defaults to False.
        iter_method ([type], optional): Метод перебора значений (какой то из list, reversed, randomly). Defaults to list.

    Returns:
        set: Минимальный набор тестов для d_plus и Q_j
    """
    t = set()
    Q_j = copy.deepcopy(Q_j_orig)
    if d_plus in Q_j:
        Q_j.remove(d_plus)
    _kw = {d_minus: kw(d_plus, d_minus) for d_minus in Q_j}
    _mw = {i: mw_method(i, d_plus, Q_j) for i in range(len(d_plus))}

    while Q_j:
        d_minus_selected = find_min(_kw, iter_method, _kw.get)
        diff_attr = {k: v for k, v in _mw.items() if k in distinguishing(d_plus, d_minus_selected)}
        attrs_selected = []

        for k, v in diff_attr.items():
            if v == find_max(diff_attr.values(), iter_method):
                attrs_selected.append(k)

        t = t.union(set(attrs_selected))
        for_deletion = []
        for d_minus in Q_j:
            if set(attrs_selected).intersection(set(distinguishing(d_minus, d_plus))):
                for_deletion.append(d_minus)
        for d in for_deletion:
            Q_j.remove(d)
            _kw.pop(d)
        if mw_recalculate:
            _mw = {i: mw_method(i, d_plus, Q_j) for i in range(len(d_plus))}
    return t


def upravl(Q_i, Q_j, poisk_alg=poisk, mw_method=mw, iter_method=list, mw_recalculate=False):
    """Реализация алгоритма upravl

    Args:
        Q_i (List[tuple]): Первый класс
        Q_j (List[tuple]): Второй класс
        poisk_alg (Callable, optional): Алгоритм поиска. Defaults to poisk.
        mw_method (Callable, optional): Алгоритм расчета mw. Defaults to mw.
        iter_method (Callable, optional): Метод перебора значений (какой то из list, reversed, randomly). Defaults to list.
        mw_recalculate (bool, optional): Нужно ли пересчитывать mw на каждом шаге. Defaults to False.

    Returns:
        set: Квази-минимальный набор тестов
    """
    T = set()
    for d_plus in Q_i:
        if poisk_alg == poisk:
            mt = poisk(d_plus, Q_j, iter_method=iter_method)
        else:
            mt = my_poisk(d_plus, Q_j, mw_method=mw_method, iter_method=iter_method, mw_recalculate=mw_recalculate)
        T = T.union(mt)
    return T


def make_qmt(data, poisk_alg=poisk, mw_method=mw, iter_method=list, mw_recalculate=False):
    """Создает матрицу квази-минимальных тестов

    Args:
        data (dict): Словарь классов
        poisk_alg (Callable, optional): Алгоритм поиска. Defaults to poisk.
        mw_method (Callable, optional): Алгоритм расчета mw. Defaults to mw.
        iter_method (Callable, optional): Метод перебора значений (какой то из list, reversed, randomly). Defaults to list.
        mw_recalculate (bool, optional): Нужно ли пересчитывать mw на каждом шаге. Defaults to False.

    Returns:
        dict: Матрица квази-минимальных тестов
    """
    qmt = defaultdict(dict)
    for i, i_elems in data.items():
        for j, j_elems in data.items():
            if j in qmt[i]:
                continue
            qmt[i][j] = upravl(i_elems, j_elems, poisk_alg=poisk_alg, mw_method=mw_method, iter_method=iter_method, mw_recalculate=mw_recalculate)
    return qmt


def classify(train, test, poisk_alg=poisk, mw_method=mw, iter_method=list, mw_recalculate=False):
    """Классификация класса при помощи DEFINE системы

    Args:
        train (dict): Входные примеры
        test (list): Тестовый набор
        poisk_alg (Callable, optional): Алгоритм поиска. Defaults to poisk.
        mw_method (Callable, optional): Алгоритм расчета mw. Defaults to mw.
        iter_method (Callable, optional): Метод перебора значений (какой то из list, reversed, randomly). Defaults to list.
        mw_recalculate (bool, optional): Нужно ли пересчитывать mw на каждом шаге. Defaults to False..

    Returns:
        str: Класс принадлежности элементов test
    """
    qmt = make_qmt(train, poisk_alg=poisk_alg, mw_method=mw_method, iter_method=iter_method, mw_recalculate=mw_recalculate)
    tests = dict()
    tests_count = defaultdict(int)
    for _cls, items in train.items():
        tests[_cls] = upravl(test, items, poisk_alg=poisk_alg, mw_method=mw_method, iter_method=iter_method, mw_recalculate=mw_recalculate)
    for _cls, class_tests in qmt.items():
        for _cls2, test_tests in tests.items():
            tests_count[_cls] += len(class_tests[_cls2].intersection(test_tests))
    return max(tests_count, key=tests_count.get)
