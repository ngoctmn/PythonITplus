_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

_list = []

for i in _tuple:
    if _tuple.count(i) == 1:
        _list.append(i)

_new_tuple = tuple(_list)

print(_new_tuple)
