#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(int_list):
    """finds a peak in a list of unsorted integers"""

    if int_list is None or int_list == []:
        return None
    low = 0
    heigh = len(int_list)
    mid = ((heigh - low) // 2) + low
    mid = int(mid)
    if heigh == 1:
        return int_list[0]
    if heigh == 2:
        return max(int_list)
    if int_list[mid] >= int_list[mid - 1] and\
            int_list[mid] >= int_list[mid + 1]:
        return int_list[mid]
    if mid > 0 and int_list[mid] < int_list[mid + 1]:
        return find_peak(int_list[mid:])
    if mid > 0 and int_list[mid] < int_list[mid - 1]:
        return find_peak(int_list[:mid])
