from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

'''
            3
           / \
          9.  20
              /\
            15  7

                   1
                  / \
     T,3       2     2 - T, 1
              /  \ 
    T,2  -   3    3 - T, 1
           /. \
          4.   4 - T, 1
'''

import collections
def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    StatusHeight = collections.namedtuple('StatusHeight', ('balanced', 'height'))
    def check_balanced(tree):
        # Base case: NULL
        if not tree:
            return StatusHeight(True, -1)

        # Ask left subtree for height and if balanced
        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return left_result

        # Ask right subtree for height and if balanced
        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return right_result
        
        # Determine if balanced, calculate height
        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return StatusHeight(is_balanced, height)
    return check_balanced(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
