from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

'''
k = 4
nodes = [7 11 13]
result = [19 17]
nodes_found = 2
'''
def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    # # O(k+h) space and time, iterative
    # result = []
    # nodes = []
    # current = tree
    # while len(result) < k:
    #     # go right 
    #     if current is not None:
    #         nodes.append(current)
    #         current = current.right
    #     elif nodes:
    #         current = nodes.pop()
    #         result.append(current.data)
    #         # go left
    #         current = current.left
    #     else:
    #         break
    # return result

    # O(k+h) space and time, recursive
    def find_k_largest_in_bst_helper(tree):
        if tree and len(result) < k:
            find_k_largest_in_bst_helper(tree.right)
            if len(result) < k:
                result.append(tree.data)
                find_k_largest_in_bst_helper(tree.left)

    result = []
    find_k_largest_in_bst_helper(tree)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
