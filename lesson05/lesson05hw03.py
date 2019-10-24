# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


def read_file():
    dct = {}
    try:
        with open("hw_03.txt", encoding="u8") as file_obj:
            for line in file_obj.readlines():
                lst = (line.strip("\n").split(','))
                dct[lst[0]] = int(lst[1])
        return dct
    except ValueError:
        print("Non integer value in salary column.")
        return 0
    except IndexError:
        print("Non valid document.")
        return 0


def sal_less(dct, lim):
    if dct != 0:
        return [k for k, v in dct.items() if v < lim]


def sal_aver(dct):
    if dct != 0:
        return round(sum(dct.values()) / len(dct), 2)


print(f"Считанные данные: {read_file()} \n")
print(f"Сотрудники с окладом менее 20 тыс.: {(sal_less(read_file(), 20000))} \n")
print(f"Средняя ЗП: {sal_aver(read_file())}")
