_tuple = ('a', 'b', 'd', 'e')
_list = list(_tuple)

_list.insert(2, 'c')
_new_tuple = tuple(_list)

print(_new_tuple)
