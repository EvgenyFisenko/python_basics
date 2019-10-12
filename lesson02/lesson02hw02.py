# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать
# функцию input().

user_list = list(input("Введите элементы массива, разделяя их пробелом: ").split())

for i in user_list:
    ind = user_list.index(i)
    prev_ind = ind - 1
    if user_list.index(i) % 2 != 0:
        user_list[ind], user_list[prev_ind] = user_list[prev_ind], user_list[ind]
print(user_list)
