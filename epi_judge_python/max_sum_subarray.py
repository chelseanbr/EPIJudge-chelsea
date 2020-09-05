from typing import List

from test_framework import generic_test


def find_maximum_subarray(A: List[int]) -> int:
    cache = max_sum = 0
    for num in A:
        cache = max(num, num + cache)
        max_sum = max(cache, max_sum)
    return max_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
