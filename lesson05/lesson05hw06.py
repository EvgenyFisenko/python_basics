# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.


def to_dict():
    dct = {}
    with open("hw_06.csv", encoding="u8") as file_obj:
        for line in file_obj.readlines():
            line_el = line.strip("\n").split(";")
            sum_if = 0
            for el in line_el:
                if el.isdigit():
                    sum_if += int(el)
            dct[line_el[0]] = sum_if
    return dct


print(to_dict())


