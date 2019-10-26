# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Время перехода между режимами должно составлять 7 и 2 секунды. Проверить работу примера, создав экземпляр и
# вызвав описанный метод.


class TrafficLight:

    def __init__(self):
        self.__color = ""

    def running(self):
        self.__color = "red"
        print(self.__color)
        for i in range(1, 8):
            print(i)
        self.__color = "yellow"
        print(self.__color)
        for i in range(1, 3):
            print(i)
        self.__color = "green"
        print(self.__color)


tl = TrafficLight()
tl.running()
