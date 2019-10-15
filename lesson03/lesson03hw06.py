# Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
# вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().


def int_func(input_str):
    return input_str.capitalize()


def int_func_text(input_str):
    out_str = ''
    for i in input_str.split():
        out_str += int_func(i) + ' '
    return out_str


print(int_func("text"))
print(int_func_text("text text text text"))
