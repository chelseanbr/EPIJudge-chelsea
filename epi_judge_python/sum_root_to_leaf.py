from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    # DFS
    if not tree:
        return 0
    cusum = 0
    nodes_vals = [(tree, tree.data)]
    while nodes_vals:
        cur_node, cur_val = nodes_vals.pop()
        if cur_node.right:
            nodes_vals.append((cur_node.right, cur_val * 2 + cur_node.right.data))
        if cur_node.left:
            nodes_vals.append((cur_node.left, cur_val * 2 + cur_node.left.data)) 
        if not cur_node.right and not cur_node.left: # Leaf node
            cusum += cur_val
    return cusum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
