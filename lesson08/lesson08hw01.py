# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, date_str):
        Date.date_str = date_str

    @classmethod
    def str_converter(cls):
        d, m, y = int(cls.date_str[:2]), int(cls.date_str[3:5]), int(cls.date_str[6:])
        return d, m, y

    @staticmethod
    def str_validator():
        d, m, y = Date.str_converter()
        if 0 <= d > 31 or 0 <= m > 12 or y > 2019:
            print("Invalid data")
        else:
            print("Data fine")


print(Date('31-10-2019').str_converter())
Date.str_validator()
