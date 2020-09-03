import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # O(h) time, O(h) space
    # Get all ancestors of first node
    first_ancestors = set()
    nodes = [node0]
    while nodes:
        node = nodes.pop()
        first_ancestors.add(node)
        if node.parent:
            nodes.append(node.parent)
    # Get each ancestor of second node, immediately return if common
    nodes = [node1]
    while nodes:
        node = nodes.pop()
        if node in first_ancestors:
            return node
        if node.parent:
            nodes.append(node.parent)

@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
