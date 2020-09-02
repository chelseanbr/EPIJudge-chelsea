from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

import collections
def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    keys_by_depth = []
    if tree:
        nodes_depths = collections.deque() # Queue to preserve order
        nodes_depths.append((tree, 0))

        while nodes_depths:
            curr_node, curr_depth = nodes_depths.popleft()
            if len(keys_by_depth) <= curr_depth:
                keys_by_depth.append([curr_node.data])
            else: 
                keys_by_depth[curr_depth].append(curr_node.data)
            if curr_node.left:
                nodes_depths.append((curr_node.left, curr_depth + 1))
            if curr_node.right:
                nodes_depths.append((curr_node.right, curr_depth + 1))
    return keys_by_depth


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
