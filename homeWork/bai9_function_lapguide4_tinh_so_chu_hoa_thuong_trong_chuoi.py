string = 'The Brow Fox'


def count_string(string):
    string_super = 0
    string_lower = 0
    for i in string:
        if i.isupper():
            string_super += 1
        elif i.islower():
            string_lower += 1
    return f'Hoa = {string_super}, Thuong = {string_lower}'


print(count_string(string))
