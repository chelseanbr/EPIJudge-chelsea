from typing import List

from test_framework import generic_test

import heapq
def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # O(n) space, O(nlogn) time
    # sorted_arrays elements --O(nlogn) time--> heap, O(n) space --O(n) time--> result array, O(n) space
    result = []
    # Get all elements from all sorted arrays, heapify
    all_elements = [item for array in sorted_arrays for item in array]
    heapq.heapify(all_elements)
    # Keep popping from heap to push to result
    while all_elements:
        result.append(heapq.heappop(all_elements))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
