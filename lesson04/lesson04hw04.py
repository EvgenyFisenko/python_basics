# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в
# порядке их следования в исходном списке. Для выполнения задания обязательно
# использовать генератор.

from random import randint


def gen_list():
    return [randint(11, 22) for el in range(10)]


def gen_uni_list():
    my_list = gen_list()
    uni_list = []
    [uni_list.append(el) for el in my_list if el not in uni_list]
    print(f"Исходный список: {my_list} \nНовый    список: {uni_list}")


gen_uni_list()
