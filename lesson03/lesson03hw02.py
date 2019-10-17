# Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_info_v1(first_name, last_name, city, email, phone):
    print(f"{first_name} {last_name} {city} {email} {phone}")


def user_info_v2(**kwargs):
    user_str = " "
    for v in kwargs.values():
        user_str += " " + v
    return user_str


def user_info_v3(**kwargs):
    user_str = " "
    for k, v in kwargs.items():
        user_str += " " + k + " " + v
    return user_str


user_info_v1(first_name="Имя", last_name="Фамилия", city="Город", email="Почта", phone="Телефон")
print(user_info_v2(first_name="Имя", last_name="Фамилия", city="Город", email="Почта", phone="Телефон"))
print(user_info_v3(first_name="Имя", last_name="Фамилия", city="Город", email="Почта", phone="Телефон"))
