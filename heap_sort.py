# -*- coding:utf-8 -*-
from heapq import *
import sys


def heap_sort(sort_arr):
    for i in range(0, len(sort_arr)):
        sort_arr[i] *= -1
    h = []
    for key in sort_arr:
        heappush(h, key)
    return [heappop(h)*-1 for _ in range(0, len(h))]


if __name__ == '__main__':
    test_arr = [0, 2, 5, 6, 7, -1]
    print heap_sort(test_arr)
