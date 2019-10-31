# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Следующий шаг — реализовать перегрузку метода __str__()
# для вывода матрицы в привычном виде. Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.


class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return '\n'.join(''.join('%5i' % i for i in el) for el in self.lst)

    def __add__(self, other):
        if len(self.lst) >= len(other.lst):
            sum_lst, add_lst = self.lst, other.lst
        else:
            sum_lst, add_lst = other.lst, self.lst
        for i in range(len(min(sum_lst, add_lst))):
            for j in range(len(sum_lst[i])):
                sum_lst[i][j] += add_lst[i][j]
        self.lst = sum_lst
        return self


mx1 = Matrix([[3, 5, 32], [2, 5, 4], [-1, 64, -8]])
mx2 = Matrix([[3, 5, 32], [2, 4, 6]])
print(mx1)
print("\n")
print(mx1 + mx2)
