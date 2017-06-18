# -*- coding:utf-8 -*-
import sys


def find_largest(sort_arr):
    res_index = 0
    res = sort_arr[0]
    for i in range(0, len(sort_arr)):
        if sort_arr[i] > res:
            res = sort_arr[i]
            res_index = i
    return res_index


def select_sort(sort_arr):
    new_arr = []
    length = len(sort_arr)
    for i in range(0, length):
        res_index = find_largest(sort_arr)
        new_arr.append(sort_arr.pop(res_index))
    return new_arr

if __name__ == '__main__':
    test_arr = [0, 2, 5, 6, 7, -1]
    print select_sort(test_arr)
