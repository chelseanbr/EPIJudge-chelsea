from typing import List

from test_framework import generic_test


def has_three_sum(A: List[int], t: int) -> bool:
    # Sort list to save space
    A.sort()
    # Use has_two_sum
    def has_two_sum(A, t):
        i = 0
        j = len(A) - 1
        while i <= j:
            two_sum = A[i] + A[j]
            if two_sum == t:
                return True
            elif two_sum > t:
                j -= 1
            else:
                i += 1
        return False
    for num in A:
        two_sum_needed = t - num
        if has_two_sum(A, two_sum_needed):
            return True
    return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
