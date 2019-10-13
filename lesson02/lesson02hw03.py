# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

winter_list = ["Зима", 12, 1, 2]
spring_list = ["Весна", 3, 4, 5]
summer_list = ["Лето", 6, 7, 8]
autumn_list = ["Осень", 9, 10, 11]
year_list = [winter_list, spring_list, summer_list, autumn_list]

user_inp = int(input("Введите порядковый номер месяца 1-12 (решение через list): \n"))
for i in year_list:
    if user_inp in i:
        print(i[0])

year_dict = {}
for i in year_list:
    year_dict[i[0]] = [i[1], i[2], i[3]]

user_inp = int(input("И еще раз. Введите порядковый номер месяца 1-12 (решение через dict): \n"))
for k, v in year_dict.items():
    if user_inp in v:
        print(k)
