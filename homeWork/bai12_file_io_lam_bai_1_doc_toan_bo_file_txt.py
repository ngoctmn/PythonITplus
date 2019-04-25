def read_file(fname):
    file = open(fname, 'r')
    s = file.read()
    print(s)


read_file('lesson8fileW.txt')
