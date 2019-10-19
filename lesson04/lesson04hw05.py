# Реализовать формирование списка, используя функцию range() и возможности генератора. В
# список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce()

from random import randrange
from functools import reduce


def gen_list():
    return [randrange(100, 1001, 2) for el in range(10)]


def sum_list(prev_el, el):
    return prev_el * el


print(reduce(sum_list, gen_list()))
