from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

import collections
def is_symmetric(root: BinaryTreeNode) -> bool:
    # # Recursively
    # def check_symmetry(left_subtree, right_subtree):
    #     # BASE CASE
    #     if not left_subtree and not right_subtree:
    #         return True
    #     elif left_subtree and right_subtree:
    #         return (left_subtree.data == right_subtree.data and check_symmetry(left_subtree.left, right_subtree.right) \
    #     and check_symmetry(left_subtree.right, right_subtree.left))
    #     else:
    #         return False
    # return not root or check_symmetry(root.left, root.right)
    
    # Iteratively
    # BFS
    q = collections.deque([])
    q.append(root)
    q.append(root)
    while q:
        t1 = q.popleft()
        t2 = q.popleft()
        if not t1 and not t2:
            continue
        if not t1 or not t2:
            return False
        if t1.data != t2.data:
            return False
        q.append(t1.left)
        q.append(t2.right)
        q.append(t1.right)
        q.append(t2.left)
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
