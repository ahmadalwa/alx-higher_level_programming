#!/usr/bin/python3
def safe_print_division(a, b):
    r = None
    try:
        r = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(r))
    return r


if __name__ == '__main__':
    safe_print_integer('s')
