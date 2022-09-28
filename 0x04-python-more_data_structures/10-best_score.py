#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    max_key = list(a_dictionary.keys())[0]
    max_big = a_dictionary[max_key]
    for key, val in a_dictionary.items():
        if val > max_big:
            max_big = val
            max_key = key
    return (max_key)
