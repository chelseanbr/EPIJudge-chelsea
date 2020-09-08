from typing import List

from test_framework import generic_test

import random
# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    def partition_around_pivot(l, r, pivot_idx):
        # New pivot idx keeps track of last swap of element > pivot
        new_pivot_idx = l #n
        pivot = A[pivot_idx]
        A[r], A[pivot_idx] = A[pivot_idx], A[r]
        for i in range(l, r):
            if A[i] > pivot:
                A[new_pivot_idx], A[i] = A[i], A[new_pivot_idx]
                new_pivot_idx += 1
        A[r], A[new_pivot_idx] = A[new_pivot_idx], A[r]
        return new_pivot_idx
    l = 0
    r = len(A) - 1
    while l <= r:
        # Randomly choose pivot in range of l to r, inclusive
        pivot_idx = random.randint(l, r) #p

        # Partition to place pivot and have elements > pivot to the left
        new_pivot_idx = partition_around_pivot(l, r, pivot_idx) 

        # Take pivot or eliminate options
        if new_pivot_idx == k-1:
            return A[new_pivot_idx]
        elif new_pivot_idx > k-1:
            r = new_pivot_idx - 1
        else: # Less than
            l = new_pivot_idx + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
