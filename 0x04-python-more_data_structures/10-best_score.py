#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None

    max = list(a_dictionary.keys())[0]
    for key in a_dictionary:
        if a_dictionary[key] > a_dictionary[max]:
            max = key
    return max
