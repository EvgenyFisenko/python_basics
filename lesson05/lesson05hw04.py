# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


def rep():
    with open("hw_04r.txt", encoding="u8") as r_file:
        for line in r_file.readlines():
            with open("hw_04w.txt", "a", encoding="u8") as w_file:
                w_file.writelines(line.replace(
                    "One", "Один").replace("Two", "Два").replace("Three", "Три").replace("Four", "Четыре"))


rep()
