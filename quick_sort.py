# -*- coding:utf-8 -*-
import sys


def quick_sort(sort_arr):
    if len(sort_arr) < 2:
        return sort_arr
    else:
        pri = sort_arr[0]
        smaller = [i for i in sort_arr[1:] if i <= pri]
        larger = [i for i in sort_arr[1:] if i > pri]
        return quick_sort(smaller) + [pri] + quick_sort(larger)

if __name__ == '__main__':
    test_arr = [0, 2, 5, 6, 7, -1]
    print quick_sort(test_arr)
