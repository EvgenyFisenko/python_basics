# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.


class Clothes:
    _cloth = 0

    def __init__(self, name, option):
        self.name = name
        self.option = option

    @property
    def craft(self):
        if self.type == "coat":
            self.cloth = round(self.option / 6.5 + 0.5, 2)
            Clothes._cloth += self.cloth
        if self.type == "suit":
            self.cloth = round(2 * self.option + 0.3, 2)
            Clothes._cloth += self.cloth
        return self.cloth

    def get_cloth(self):
        print(f"Всего использованно ткани: {round(Clothes._cloth, 2)}")


class Coat(Clothes):

    def __init__(self, name, option):
        super().__init__(name, option)
        self.type = "coat"


class Suit(Clothes):

    def __init__(self, name, option):
        super().__init__(name, option)
        self.type = "suit"


c1 = Coat("my_coat_name", 20)
print(c1.name, c1.option, c1.type, c1.craft)
c1.get_cloth()

s1 = Suit("my_suit_name", 20)
print(s1.name, s1.option, s1.type, s1.craft)
s1.get_cloth()

