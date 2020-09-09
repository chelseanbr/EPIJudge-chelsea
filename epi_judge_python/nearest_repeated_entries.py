from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    # O(n) time, O(n) space
    min_distance = float('inf')
    # Hash table to store strings (all lowered) and last idx seen at
    str_last_idx = {}
    for i, string in enumerate(paragraph):
        string = string.lower()
        if string in str_last_idx:
            curr_distance = i - str_last_idx[string]
            min_distance = min(min_distance, curr_distance) 
        str_last_idx[string] = i
    if min_distance == float('inf'):
        return -1
    else:
        return min_distance


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
