def print_info(arg1, *var):
    print('Ket qua la: ')
    print(arg1)
    for v in var:
        print(v)
    return

print_info(10)
print_info(70, 60, 50)