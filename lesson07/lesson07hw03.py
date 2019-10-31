# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n**


class Cell:
    def __init__(self, unit):
        self.unit = "*" * unit

    def __add__(self, other):
        return self.unit + other.unit

    def __sub__(self, other):
        if len(self.unit) - len(other.unit) <= 0: print("разность количества ячеек двух клеток меньше нуля")
        return '*' * (len(self.unit) - len(other.unit))

    def __mul__(self, other):
        return '*' * (len(self.unit) * len(other.unit))

    def __truediv__(self, other):
        return '*' * (len(self.unit) // len(other.unit))

    def make_order(self, order):
        res = ''
        i = len(self.unit)
        while i > order:
            res += ('*' * order + r'\n')
            i -= order
        res += ('*' * i)
        return res


c1 = Cell(12)
c2 = Cell(2)
print(c1.unit)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c1.make_order(5))
