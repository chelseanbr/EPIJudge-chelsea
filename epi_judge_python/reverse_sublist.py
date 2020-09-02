from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    # O(n) time, O(1) space
    dummy_head = sublist_h = ListNode(0, L)
    for _ in range(1, start):
        sublist_h = sublist_h.next
    sublist_i = sublist_h.next
    for _ in range(finish - start):
        temp = sublist_i.next
        sublist_i.next = temp.next
        temp.next = sublist_h.next
        sublist_h.next = temp
    return dummy_head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
