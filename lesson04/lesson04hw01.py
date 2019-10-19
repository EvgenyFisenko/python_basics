# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

my_time, my_price, my_bonus = argv[1:]


def salary(time, price, bonus):
    try:
        sal = int(time) * int(price) + int(bonus)
        return sal
    except ValueError:
        print("Допустимы только целочисленные значения")
        return 0


print(salary(my_time, my_price, my_bonus))
