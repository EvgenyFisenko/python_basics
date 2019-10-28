# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"profit": profit, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_full_profit). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
#  проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"profit": profit, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_full_profit(self):
        print(self._income['profit'] + self._income['bonus'])


p1 = Position("Vasya", "Pupkin", "QA", 900, 211)
print(p1.name, p1.surname, p1.position, "\n")

p1.get_full_name()
p1.get_full_profit()
