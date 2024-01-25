#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    ints = [dictionary[x] for x in roman_string]
    result = 0
    for i in range(len(ints)):
        result += ints[i]
        if ints[i - 1] < ints[i] and i != 0:
            result -= (ints[i - 1] + ints[i - 1])
    return result
