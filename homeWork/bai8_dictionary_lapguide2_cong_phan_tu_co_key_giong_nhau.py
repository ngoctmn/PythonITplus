d1 = {'a': 15, 'b': 20, 'c': 30, 'e': 60}
d2 = {'a': 30, 'b': 20, 'd': 50}
d3 = dict()

# Cach 1: Khong duoc => error
# for key, value in d2.items():
#     if key in d1.keys():
#         value += d1[key]
#     else:
#         value = d1[key]
#     d3.update({key: value})
#
# print(d3)

# Cach 2:
for k,v in d2.items():
    if k in d1:
        d1[k] += v
    else:
        d1[k] = v

print(d1)
