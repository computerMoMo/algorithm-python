# -*- coding:utf-8 -*-
import sys


def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result


def merge_sort(res_arr):
    if len(res_arr) <= 1:
        return res_arr
    else:
        mid = len(res_arr)/2
        left = merge_sort(res_arr[:mid])
        right = merge_sort(res_arr[mid:])

        return merge(left, right)

if __name__ == '__main__':
    test_arr = [0, 2, 5, 6, 7, -1]
    print merge_sort(test_arr)
    print test_arr[0:]
    print test_arr[:0]
