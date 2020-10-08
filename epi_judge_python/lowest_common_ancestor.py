import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

import collections
def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # Recursive
    Status = collections.namedtuple('Status',('num_target_nodes', 'lca'))
    def recurse_tree(cur_node, p, q):
        if not cur_node:
            return Status(num_target_nodes=0, lca=None)            
        left = recurse_tree(cur_node.left, p, q)
        if left.num_target_nodes == 2:
            return left
        right = recurse_tree(cur_node.right, p, q)
        if right.num_target_nodes == 2:
            return right
        num_target_nodes = (left.num_target_nodes + \
            right.num_target_nodes + (p, q).count(cur_node))

        if num_target_nodes >= 2:
            lca = cur_node
        else:
            lca = None
        return Status(num_target_nodes, lca)
    return recurse_tree(tree, node0, node1).lca

    # # Recursive, O(n) time, O(n) space
    # if not tree:
    #     return None
    # # Return tree if node 1 or 2 
    # if node0.data == tree.data or node1.data == tree.data:
    #     return tree
    # # Search left and right
    # left_search_result = lca(tree.left, node0, node1)
    # right_search_result = lca(tree.right, node0, node1)

    # if not left_search_result:
    #     return right_search_result
    # if not right_search_result:
    #     return left_search_result
    # # Return tree once both node 1 and 2 found to the left and right
    # return tree # Both left_search_result and right_search_result


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
