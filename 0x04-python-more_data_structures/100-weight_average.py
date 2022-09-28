#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    avg_score = 0
    size_wght = 0
    for tup in my_list:
        avg_score += (tup[0] * tup[1])
        size_wght += tup[1]
        return (avg_score / size_wght)
