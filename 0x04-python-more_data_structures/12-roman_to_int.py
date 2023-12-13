#!/usr/bin/python3
__tiers = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
__romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    }


def _ts(ln):
    ts = 0
    ml = max(ln)
    for n in ln:
        if ml > n:
            ts += n
    return (ml - ts)


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    num = 0
    lr = 0
    ln = [0]
    for ch in roman_string:
        for r_num in __tiers:
            if r_num == ch:
                if __romans.get(ch) <= lr:
                    num += _ts(ln)
                    ln = [__romans.get(ch)]
                else:
                    ln.append(__romans.get(ch))

                lr = __romans.get(ch)
    num += _ts(ln)
    return num


def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    roman_string = roman_string.upper()
    # split the string to [num minus num]
    num_parts = []
    break_loop = 0
    while True:
        previous_tier = -1
        roman_string_len = len(roman_string)
        for idx, c in enumerate(tuple(roman_string)):
            current_tier = __tiers.index(c)
            if current_tier >= previous_tier:
                previous_tier = current_tier
                if idx == roman_string_len - 1:
                    num_parts.append(roman_string)
                    # roman_string = ''
                    break_loop = 1
                    break
                else:
                    continue
            else:
                num_parts.append(roman_string[:idx])
                roman_string = roman_string[idx:]
                break

        if break_loop:
            break

    num = 0
    # print(num_parts)
    for i in num_parts:
        total = 0
        tier = -1
        for c in i:
            part = __romans[c]
            _tier = __tiers.index(c)
            if _tier > tier:
                total = part - total
            elif _tier == tier:
                total += part
            tier = _tier
        num += total
    return num


if __name__ == '__main__':
    # print(roman_to_int('IIXCDI'))
    """
    X = 10
    VII = 7
    IX = 9
    LXXXVII = 87
    DCCVII = 707
    """
    roman_numerals = dict([
        ('MCMXCVIII', 1998),
        ('MDCLXVI', 1666),
        ('MMXIX', 2019),
        ('MMMDCCCXCII', 3392),
        ('MMMM', 4000),
        ('MCMXCIX', 1999),
        ('MMCCCXCVII', 2397),
        ('MMCCCXXXIII', 2333),
        ('MMMDCCLXIX', 3369),
        ('MMMDCCLXXXVIII', 3388),
        ('MMMDCCLXXVII', 3377),
        ('MMMDCCLXXVI', 3376),
        ('MMMDCCLXXV', 3375),
        ('MMMDCCLXXIV', 3374),
        ('MMMDCCLXXIII', 3373),
        ('MMMDCCLXXII', 3372),
        ('MMMDCCLXXI', 3371),
        ('MMMDCCLXX', 3370),
        ('MMMDCCLXIX', 3369),
        ('MMMDCCLXVIII', 3368),
        ('MMMDCCLXVII', 3367),
        ('MMMDCCLXVI', 3366),
        ('MMMDCCLXV', 3365),
        ('MMMDCCLXIV', 3364),
        ('MMMDCCLXIII', 3363),
        ('MMMDCCLXII', 3362),
        ('MMMDCCLXI', 3361),
        ('MMMDCCLX', 3360),
        ('MMMDCCLXIX', 3369),
        ('MMMDCCLXVIII', 3368),
        ('MMMDCCLXVII', 3367),
        ('MMMDCCLXVI', 3366),
        ('MMMDCCLXV', 3365),
        ('MMMDCCLXIV', 3364),
        ('MMMDCCLXIII', 3363),
        ('MMMDCCLXII', 3362),
        ('MMMDCCLXI', 3361),
        ('MMMDCCLX', 3360),
        ('MMMDCCLXIX', 3369),
        ('MMMDCCLXVIII', 3368),
        ('MMMDCCLXVII', 3367),
        ('MMMDCCLXVI', 3366),
        ('MMMDCCLXV', 3365),
        ('MMMDCCLXIV', 3364),
        ('MMMDCCLXIII', 3363),
        ('MMMDCCLXII', 3362),
        ('MMMDCCLXI', 3361),
        ('MMMDCCLX', 3360),
        ('MMMDCCLXIX', 3369),
        ('MMMDCCLXVIII', 3368),
        ('MMMDCCLXVII', 3367),
        ('MMMDCCLXVI', 3366),
        ('MMMDCCLXV', 3365),
        ('MMMDCCLXIV', 3364),
        ('MMMDCCLXIII', 3363),
        ('MMMDCCLXII', 3362),
        ('MMMDCCLXI', 3361),
        ('MMMDCCLX', 3360),
        ('MMMDCCLXIX', 3369),
        ('MMMDCCLXVIII', 3368),
        ('MMMDCCLXVII', 3367),
        ('MMMDCCLXVI', 3366),
        ('MMMDCCLXV', 3365),
        ('MMMDCCLXIV', 3364),
        ('MMMDCCLXIII', 3363),
        ('MMMDCCLXII', 3362),
        ('MMMDCCLXI', 3361),
        ('MMMDCCLX', 3360),
        ('MMMDCCLXIX', 3369),
        ('MMMDCCLXVIII', 3368),
        ('MMMDCCLXVII', 3367),
        ('MMMDCCLXVI', 3366),
        ('MMMDCCLXV', 3365),
        ('MMMDCCLXIV', 3364),
        ('MMMDCCLXIII', 3363),
        ('MMMDCCLXII', 3362),
        ('MMMDCCLXI', 3361),
        ('MMMDCCLX', 3360),
        ('MMMDCCLXIX', 3369),
        ('MMMDCCLXVIII', 3368),
        ('MMMDCCLXVII', 3367),
        ('MMMDCCLXVI', 3366),
        ('MMMDCCLXV', 3365),
        ('MMMDCCLXIV', 3364),
        ('MMMDCCLXIII', 3363),
        ('MMMDCCLXII', 3362),
        ('MMMDCCLXI', 3361),
        ('MMMDCCLX', 3360),
        ('MMMDCCLXIX', 3369),
        ('MMMDCCLXVIII', 3368),
    ])

    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000,
                 'IV': 4, 'IX': 9, 'XL': 40,
                 'XC': 90, 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in roman:
                num += roman[s[i:i + 2]]
                i += 2
            else:
                # print(i)
                num += roman[s[i]]
                i += 1
        return num

    for k in roman_numerals:
        _int = roman_to_int(k)
        v = romanToInt(k)
        if v != _int:
            print(f'Failed {k} == {v} not {_int}')
    print('done')
