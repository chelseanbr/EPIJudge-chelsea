from typing import List

from test_framework import generic_test

import heapq
def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # O(n) space, O(2*nlogk) ~ O(nlogk) time
    # sorted_arrays elements --O(nlogk) time--> heap, O(k) space --O(nlogk) time--> result array, O(n) space
    result = []
    # Put max k elements into heap
    min_heap = []
    array_iters = [iter(x) for x in sorted_arrays]

    # init heap
    for i, it in enumerate(array_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    # # Pop min from heap, add next val to heap, if any
    while min_heap:
        curr_min_element, curr_min_arr = heapq.heappop(min_heap)
        curr_arr_iter = array_iters[curr_min_arr]
        next_element = next(curr_arr_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, curr_min_arr))
        result.append(curr_min_element)
    return result

    # Pythonic
    # return list(heapq.merge(*sorted_arrays))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
