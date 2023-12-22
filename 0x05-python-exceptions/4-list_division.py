#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    r = [0 for i in range(list_length)]
    for i in range(list_length):
        d = 0
        try:
            a = my_list_1[i]
            b = my_list_2[i]
        except IndexError:
            print("out of range")
            continue
        try:
            d = a / b
        except ZeroDivisionError:
            print("division by 0")
        except (TypeError, ValueError):
            print("wrong type")
        finally:
            r[i] = d
    return r


if __name__ == '__main__':
    safe_print_integer('s')
