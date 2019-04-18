inlist = [5, 8, 11, 9, 11, 8, 8]

def remove_list(input_list, del_list):
    for i in del_list:
        for j in range(input_list.count(i)):
            input_list.remove(i)

    return input_list


del_list = [8, 11]
print(remove_list(inlist, del_list))