my_list = [1, 4, 5, 6, 7]


def element_at(my_list):
    idx = int(input("what is your index: "))
    if idx > len(my_list) and idx < 0:
        return None
    else:
        print("Element at {} is: {}".format(idx, my_list[idx]))


element_at(my_list)
