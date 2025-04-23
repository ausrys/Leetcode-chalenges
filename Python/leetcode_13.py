'''
Given a roman numeral, convert it to an integer.
'''


def roman_to_int(s: str) -> int:
    total_sum = 0
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i, roman in enumerate(s):
        if i < len(s) - 1 and romans[s[i]] < romans[s[i + 1]]:
            total_sum -= romans[roman]
        else:
            total_sum += romans[roman]
    return total_sum


print(roman_to_int("MCMXCIV"))
