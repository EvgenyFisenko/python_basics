# Создайте собственный класс-исключение, который должен проверять содержимое списка на отсутствие элементов типа строка
# и булево. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
# список. Класс-исключение должен контролировать типы данных элементов списка.


class MyErr(Exception):
    def __init__(self, text):
        self.text = text


def my_list():
    lst = []
    while len(lst) < 5:
        try:
            a = input("Введите число: ")
            if isinstance(a, bool) or not a.isdigit():
                raise MyErr("Только целые числа")
        except MyErr as err:
            print(err)
            continue
        else:
            a = int(a)
            lst.append(a)
            print(lst)


my_list()
