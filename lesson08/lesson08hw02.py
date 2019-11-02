# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class MyErr(Exception):
    def __init__(self, text):
        self.text = text


def my_div():
    while True:
        try:
            a, b = int(input("Делимое: ")), int(input("Делитель: "))
            if b <= 0: raise MyErr("Не лучший день для деления на 0")
        except MyErr as err:
            print(err)
        else:
            return a // b


print(my_div())
