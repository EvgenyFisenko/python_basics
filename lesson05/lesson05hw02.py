# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


def text_count():
    ln_cnt, wd_cnt = 0, 0
    with open("hw_02.txt", encoding="u8") as file_obj:
        for line in file_obj.readlines():
            ln_cnt += 1
            wd_cnt += len(line.split())
    return ln_cnt, wd_cnt


print(f"Строк в файле: {text_count()[0]}. Слов в файле: {text_count()[1]}.")
