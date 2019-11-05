# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве  единиц оргтехники, а также
# других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


class Stocks:
    __count = 0
    __id = 1

    def __init__(self, location):
        loc = ["Central", "Moscow"]
        if location in loc:
            self.city = location
            self.stock = {}
            Stocks.__count += 1
        else:
            raise MyErr(f"Sorry, only {loc} is available")

    def __str__(self):
        return f"Stock name: {self.city}, stock items: {self.stock}"

    def add_item(self, item):
        self.stock.update({Stocks.__id: {'type': item.type, 'properties': item.do, 'price': item.price, 'count': 1}})
        Stocks.__id += 1

    def del_item(self, id):
        del (self.stock[id])

    def move_item(self, other, id):
        other.stock.update({id: self.stock[id]})
        del (self.stock[id])

    @staticmethod
    def get_stocks_count():
        print(f"Stocks count: {Stocks.__count}")
        return Stocks.__count


class Technics:
    __cost = 0

    def __init__(self, price):
        if isinstance(price, int):
            self.price = price
            Technics.__cost += price
        else:
            raise MyErr("Sorry. Only int")

    @property
    def do(self):
        if self.type == 'printer':
            tmp = 'print'
        if self.type == 'scanner':
            tmp = 'scan'
        if self.type == 'copier':
            tmp = 'copy'
        return tmp

    def __str__(self):
        return f"Type: {self.type}, property: {self.do}, price: {self.price} $"

    @classmethod
    def get_full_price(cls):
        print(f"Total equipment purchased on: {cls.__cost} $")
        return cls.__cost


class Printer(Technics):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.type = "printer"


class Scanner(Technics):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.type = "scanner"


class Copier(Technics):
    def __init__(self, quantity):
        super().__init__(quantity)
        self.type = "copier"


class MyErr(Exception):
    def __init__(self, text):
        self.text = text


pr, sc, cp = Printer(200), Scanner(180), Copier(150)
print(pr, '||', sc, '||', cp)
Technics.get_full_price()
Central_st = Stocks("Central")
Moscow_st = Stocks("Moscow")
Stocks.get_stocks_count()
Central_st.add_item(pr)
Central_st.add_item(pr)
Central_st.add_item(sc)
Central_st.add_item(sc)
Central_st.add_item(cp)
print(Central_st)
Central_st.del_item(1)
print(Moscow_st)
Central_st.move_item(Moscow_st, 3)
print(Central_st)
print(Moscow_st)
