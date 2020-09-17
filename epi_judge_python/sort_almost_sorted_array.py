from typing import Iterator, List

from test_framework import generic_test

import heapq
def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    # O(n log k) time, O(k) space in addition to O(n) result
    result = []
    # Init heap with first k items
    min_heap = []
    i = 0
    while i < k:
        item = next(sequence, None)
        if item is not None:
            heapq.heappush(min_heap, item)
            i += 1
    # Go through rest of the array and use heap to get next min
    while min_heap:
        item = next(sequence, None)
        if item is not None:
            result.append(heapq.heappushpop(min_heap, item))
        else:
            result.append(heapq.heappop(min_heap))
    return result


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
