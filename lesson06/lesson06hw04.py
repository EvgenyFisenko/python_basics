# Опишите несколько классов: TownCar, SportCar, WorkCar, PoliceCar. У каждого класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также несколько методов: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).


class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        print("going forward")

    def stop(self):
        print("stopped")

    def turn(self, direction):
        if direction in ["left", "right"]:
            print(f"turned {direction}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


p1 = SportCar("200", "red", "sport")
print(f"{p1.name} car is_police value = {p1.is_police}")

p2 = PoliceCar("100", "white", "police")
print(f"{p2.name} car is_police value = {p2.is_police} \n")

p1.go()
p1.turn("left")
p1.turn("right")
p1.stop()
