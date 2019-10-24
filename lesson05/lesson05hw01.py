# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


def user_inp():
    while True:
        user_input = input("Введите данные для записи в файл: ")
        if user_input == "":
            break
        with open("hw_01.txt", "a", encoding="u8") as file_obj:
            file_obj.writelines(user_input + '\n')
    print("Данные записаны!")


user_inp()
