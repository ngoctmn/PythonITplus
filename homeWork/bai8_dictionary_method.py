_contacts = {"An": "012", "Binh": "411", "Tam": "217"}

x = str(_contacts)
print(x[:5])


# Phuong thuc dict
print(_contacts.copy())

print(_contacts.clear())

a = _contacts.fromkeys(['a', 'b'], "012")
b = _contacts.fromkeys(['a', 'b'])

print(a)
print(b)


_dict = {'1': "one", 2: "two"}

# c = _dict.get('1', default = None)  # Khong duoc
# print(c)


# print(_dict.has_key(2))               # Khong duoc

print(_dict.item())