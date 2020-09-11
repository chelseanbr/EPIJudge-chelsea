from typing import List

from test_framework import generic_test

import heapq
import collections
def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    def merge_sorted_arrays(sorted_arrays):
        # In our heap, we want to store current item per array and array ID
        array_iters = [iter(x) for x in sorted_arrays]

        # Add first item per array into min heap
        min_heap = []
        for arr_id, it in enumerate(array_iters):
            item = next(it, None)
            if itemis not None:
                heapq.heappush(min_heap, (item, arr_id))

        result = []
        while min_heap:
            item, arr_id = heapq.heappop(min_heap)
            result.append(item)
            next_item = next(array_iters[arr_id], None)
            if next_item is not None:
                heapq.heappush(min_heap, (next_item, arr_id))
        return result

        # # Pythonic
        # return list(heapq.merge(*sorted_arrays))

    # Split A into k sorted arrays
    

    # Merge k arrays with helper
    return merge_sorted_arrays(sorted_arrays)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
