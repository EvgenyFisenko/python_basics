# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(a, b):
    try:
        return round(int(a) / int(b), 2)
    except ValueError:
        return "Допустимы только целые числа."
    except ZeroDivisionError:
        return "На ноль делить нельзя."


print(division(input("Делимое: "), (input("Делитель: "))))
