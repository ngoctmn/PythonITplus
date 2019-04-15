_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five'
}

print(_dict.items())
print(_dict.keys())
# _dict.setdefault(1, default=None)

_dict2 = {
    6: 'six',
    7: 'seven'
}

_dict.update(_dict2)
print(_dict)
print(_dict.values())