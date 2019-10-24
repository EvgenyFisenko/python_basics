# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
# форма собственности, выручка, издержки. Необходимо вычислить прибыль каждой компании и среднюю прибыль.
# Реализовать список, содержащий словарь (название фирмы и прибыль) и словарь с одним элементом (средняя прибыль).
# Добавить в первый словарь еще один элемент, содержащий результат вычисления отношения прибыли к убыткам.
# Итоговый список сохранить в файл.
import json


def cr_dict():
    dct = {}
    with open("hw_07r.txt", encoding="u8") as r_file:
        for line in r_file.readlines():
            lst = (line.strip("\n").split(','))
            dct[lst[0]] = {"type": lst[1], "profit": lst[2], "costs": lst[3]}
    return dct


def salary(dct):
    aver_sal = 0
    sal_dct = {}
    aver_sal_dct = {}
    for k, v in dct.items():
        sal = int(v["profit"]) - int(v["costs"])
        sal_dct[k] = {"salary": sal}
        aver_sal += sal
    aver_sal_dct["average salary"] = aver_sal / len(dct)
    return [sal_dct, aver_sal_dct]


def profitability(lst, dct):
    for el in dct:
        lst[0][el]["profitability"] = round(lst[0][el]["salary"] / int(dct[el]["costs"]), 2)
    return lst


def prof_print(p_lst):
    with open("hw_07w.txt", "w", encoding="u8") as w_file:
        json.dump(p_lst, w_file, ensure_ascii=False, indent=4)


print(f"Первый список: \n {salary(cr_dict())}")
print(f"Второй список: \n {profitability(salary(cr_dict()), cr_dict())}")

prof_print(profitability(salary(cr_dict()), cr_dict()))
