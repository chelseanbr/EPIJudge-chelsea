from typing import List

from test_framework import generic_test

import bisect
def search_first_of_k(A: List[int], k: int) -> int:
    # O(1) space, O(log n) time
    idx = -1
    L = 0
    U = len(A) - 1
    while L <= U:
        M = L + (U-L) // 2
        if A[M] < k: # move window to right of midpt
            L = M+1
        elif A[M] >= k: # move window to left of midpt
            U = M-1
            if A[M] == k: # update idx since found key
                idx = M
    return idx

    # # Python built-in binary search: bisect_left
    # idx = bisect.bisect_left(A, k)
    # if 0 <= idx < len(A) and A[idx] == k:
    #     return idx
    # else:
    #     return -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
