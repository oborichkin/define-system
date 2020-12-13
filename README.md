# Реализация алгоритмов POISK и UPRAVL системы DEFINE

Данный репозиторий содержит реализацию алгоритмов `POISK` и `UPRAVL` описанных в статье [Computing Approximately minimal diagnostic tests](https://www.researchgate.net/publication/283484938_Computing_approximately_minimal_diagnostic_tests).

Также в репозитории имеется моя тестовая реализация модифицированного алгоритма `POISK`.

## Installation

```bash
pip install .
```

## CLI Usage
```bash
$define -h
usage: define [-h] train test

Classify element using DEFINE system

positional arguments:
  train       Path to train CSV file
  test        Path to test CSV file

optional arguments:
  -h, --help  show this help message and exit
```

## Contributors

 * [Vladimir Parkhomenko](https://github.com/ParkhomenkoV)
 * Xenia Naidenova