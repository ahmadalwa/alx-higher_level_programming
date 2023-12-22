#!/usr/bin/python3
def magic_calculation(a, b):
    r = 0
    for i in range(1, 3):
        try:
            if a < i:
                raise Exception("s")
            r += a ** b / i
        except Exception as s:
            r = b + a
            break
    return r
