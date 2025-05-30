# Given an integer, convert it to a Roman numeral.

def int_to_roman(num: int) -> str:
    val_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100,  'C'), (90,  'XC'), (50,  'L'), (40,  'XL'),
        (10,   'X'), (9,   'IX'), (5,   'V'), (4,   'IV'), (1, 'I')
    ]

    roman = []
    for value, symbol in val_map:
        count, num = divmod(num, value)
        roman.append(symbol * count)
    return ''.join(roman)
