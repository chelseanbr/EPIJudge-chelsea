from typing import List

from test_framework import generic_test


def search_smallest(A: List[int]) -> int:
    shiftArr = A
    # find pivot with binary search
    l = 0
    r = len(shiftArr) - 1
    while l < r:
        m = l + (r-l)//2
        if shiftArr[m] > shiftArr[r]:
            l = m + 1
        else:
            r = m
    # pivot at l
    return l


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
