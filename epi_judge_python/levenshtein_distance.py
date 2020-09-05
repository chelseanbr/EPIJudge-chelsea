from test_framework import generic_test

import numpy as np
def levenshtein_distance(A: str, B: str) -> int:
    # DP: O(a*b) time, O((a+1)*(b+1)) space ~ O(a*b) space
    '''
      " c a t
    " 0 1 2 3
    a 1 1 1 2
    c 2 1 2 2
    t 3 2 2 2
    
    '''
    # init cache - numpy
    # cache = np.zeros((len(B)+1, len(A)+1))
    # cache[0,:] = np.arange(len(A)+1)
    # cache[:,0] = np.arange(len(B)+1)

    # init cache - 2D array
    cache = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
    cache[0] = list(range(len(A)+1))
    for i in range(len(B)+1):
        cache[i][0] = i

    for i in range(1, len(B)+1):
        for j in range(1, len(A)+1):
            if B[i-1] == A[j-1]:
                cache[i][j] = cache[i-1][j-1]
            else:
                cache[i][j] = min(cache[i-1][j-1], cache[i][j-1], cache[i-1][j]) + 1
    return cache[-1][-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
