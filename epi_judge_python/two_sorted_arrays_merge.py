from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0 :
        if B[j] > A[i]:
            A[k] = B[j]
            j -= 1
        else:
            A[k] = A[i]
            i -= 1
        k -= 1
    while j >= 0:
        A[k] = B[j]
        j -= 1
        k -= 1
    return A


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
