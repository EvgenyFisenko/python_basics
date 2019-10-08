# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_sec = int(input("Введите количество секунд: "))
hours = user_sec // 3600
minutes = (user_sec - hours * 3600) // 60
seconds = user_sec - hours * 3600 - minutes * 60

print(f"{user_sec} секунд = {hours}:{minutes}:{seconds}")
