#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end='')
            i += 1
        except IndexError:
            break
    print("")
    return i


if __name__ == '__main__':
    my_list = [1, 2, 3, 4]
    x = len(my_list)

    nb_print = safe_print_list(my_list, x)
    print("{:d}".format(nb_print))
