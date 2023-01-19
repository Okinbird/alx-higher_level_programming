#!/usr/bin/python3
"""Test function find_peak"""


def find_peak(list_of_integers):
    """finds a peak"""

    new_l = list_of_integers
    le = len(new_l)
    if le == 0:
        return
    m = le // 2
    if (m == le - 1 or new_l[m] >= new_l[m + 1]) and (m == 0 or new_l[m]
                                                      >= new_l[m - 1]):
        return new_l[m]
    if m != le - 1 and new_l[m + 1] > new_l[m]:
        return find_peak(new_l[m + 1:])
    return find_peak(new_l[:m])
