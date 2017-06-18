# -*- coding:utf-8 -*-
import sys


def binary_search(search_list, key):
    temp_list = sorted(search_list)
    low = 0
    high = len(temp_list) - 1
    mid = 0
    while low <= high:
        mid = (low+high)/2
        if temp_list[mid] > key:
            high = mid-1
        elif temp_list[mid] == key:
            return mid
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    test_list = [0, 1, 5, 6, 7, 8, 9]
    print binary_search(test_list, 5)
    print binary_search(test_list, 10)
