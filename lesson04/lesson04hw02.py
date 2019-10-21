# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

from random import randint


def gen_list():
    return [randint(11, 22) for el in range(10)]


def gen_big_list():
    my_list = gen_list()
    bg_list = [my_list[el] for el in range(len(my_list)) if my_list[el] > my_list[el - 1]]
    print(f"Исходный список: {my_list} \nНовый    список: {bg_list}")


gen_big_list()
