# -*- coding:utf-8 -*-
import sys
from heapq import *


def quick_sort2(sort_arr):
    if len(sort_arr) <= 1:
        return sort_arr
    else:
        pri = sort_arr[0]
        smaller_arr = [i for i in sort_arr[1:] if i <= pri]
        larger_arr = [i for i in sort_arr[1:] if i > pri]
        return quick_sort2(smaller_arr) + [pri] + quick_sort2(larger_arr)


def heap_sort(sort_arr):
    heap_arr = []
    for i in sort_arr:
        heappush(heap_arr, i)
    return [heappop(heap_arr) for _ in range(0, len(sort_arr))]


def find_largest(sort_arr):
    largest_num = sort_arr[0]
    largest_id = 0
    for i in range(1, len(sort_arr)):
        if sort_arr[i] > largest_num:
            largest_num = sort_arr[i]
            largest_id = i
    return largest_id


def select_sort(sort_arr):
    res_arr = []
    for _ in range(0, len(sort_arr)):
        res_arr.append(sort_arr.pop(find_largest(sort_arr)))
    return res_arr


def merge(left_arr, right_arr):
    i = 0
    j = 0
    res_arr = []
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            res_arr.append(left_arr[i])
            i += 1
        else:
            res_arr.append(right_arr[j])
            j += 1
    res_arr += left_arr[i:]
    res_arr += right_arr[j:]
    return res_arr


def merge_sort(sort_arr):
    if len(sort_arr) <= 1:
        return sort_arr
    else:
        mid = len(sort_arr)/2
        return merge(merge_sort(sort_arr[0:mid]), merge_sort(sort_arr[mid:]))

if __name__ == '__main__':
    test_arr = [0, 2, 5, 6, 7, -1]
    print merge_sort(test_arr)
