import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    # O(1) space, O(n) time - 2 passes, forward then backward
    # Forward: del 'b' and count 'a'
    write_idx = 0
    a_count = 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1
    # Backward: replace 'a' with 'd', 'd'
    curr_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    while curr_idx >= 0:
        if s[curr_idx] != 'a':
            s[write_idx] = s[curr_idx]
            write_idx -= 1
        else:
            s[write_idx - 1], s[write_idx] = 'd', 'd'
            write_idx -= 2
        curr_idx -= 1
    return final_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
