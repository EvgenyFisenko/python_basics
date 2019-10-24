def to_dict():
    dct = {}
    with open("hw_06.csv") as file_obj:
        for line in file_obj.readlines():
            elem_in = line.strip("\n").split(";")
            sum_of = 0
            for el in elem_in:
                if el.isdigit():
                    sum_of += int(el)
            dct[elem_in[0]] = sum_of
    return dct


print(to_dict())
