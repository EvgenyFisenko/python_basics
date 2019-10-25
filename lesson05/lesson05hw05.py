# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random as rnd


def cr_file():
    with open("hw_05.txt", "w", encoding="u8") as w_file:
        lst = [rnd.randrange(100, 1001, 2) for el in range(10)]
        w_file.writelines(' '.join(map(str, lst)))
        return lst, sum(lst)  # calculation check


def sum_file():
    with open("hw_05.txt", encoding="u8") as r_file:
        for line in r_file.readlines():
            return sum(map(int, line.split()))


print(cr_file())
print(sum_file())
