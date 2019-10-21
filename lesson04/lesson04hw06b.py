#  бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее

from random import randint
from itertools import cycle


def gen_list():
    return [randint(11, 22) for el in range(10)]


def my_cycle():
    lst = (gen_list())
    print(lst)
    for i in cycle(lst):
        print(i)


my_cycle()
