_list = [(1, 2), (2, 6), (3, 1, 5)]

res = sorted(_list, key=lambda tup:tup[-1], reverse=True)
print(res)

