d = {"IV": "S001", "V": "S002", "VI": "S001", "VII": "S005", "VIII": "S005", "IX": "S009", "X": "S007"}

_list = list()

for i in d.values():
    if i not in _list:
        _list.append(i)

print(_list)
