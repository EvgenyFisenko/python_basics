# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [2, 'text', 45.3, None, True, (1, 2)]
new_list = []

for i in my_list:
    new_list.append(str(type(i))[8:-2])
new_dict = dict(zip(my_list, new_list))

print(new_dict)
