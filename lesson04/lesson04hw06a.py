# бесконечный итератор, генерирующий целые числа, начиная с указанного

from itertools import count
from sys import argv


def checked_var():
    try:
        return int((argv[1]))
    except IndexError:
        print("Ошибка. Не указано значение, цикл начнется с 0.")
        return 0
    except ValueError:
        print("Ошибка. Допустимы только целые числа, цикл начнется с 0.")
        return 0


def my_cycle():
    for el in count(checked_var()):
        print(el)


my_cycle()
