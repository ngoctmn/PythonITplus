_info = {"Name": "Tran", "Age": 37, "Address": "Vietnam"}
_info.update({'key_1': 'value_1', "Name": "Update name"})

print(_info)

a = _info.keys()
print(a)
print(len(_info))
print(str(_info))
print(type(_info))
print(dir(_info))

# Xoa phan tu dict
del _info["key_1"]
print(_info)

_info.__delitem__("Age")
print(_info)

_info.clear()
print(_info)

del _info
print(_info)
