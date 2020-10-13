from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # # Recursive
    # def helper(tree, result):
    #     if not tree:
    #         return
    #     helper(tree.left, result)
    #     result.append(tree.data)
    #     helper(tree.right, result)
    # result = []
    # helper(tree, result)
    # return result

    # # Iterative with bools
    # if not tree:
    #     return []
    # inorder = []
    # nodes_visited = [(tree, False)] # cur_node, bool True if left visited
    # while nodes_visited:
    #     cur_node, visited = nodes_visited.pop()
    #     if visited:
    #         inorder.append(cur_node.data)
    #     else:
    #         if cur_node.right:
    #             nodes_visited.append((cur_node.right, False))
    #         nodes_visited.append((cur_node, True))
    #         if cur_node.left:
    #            nodes_visited.append((cur_node.left, False))
    # return inorder

    # Iterative with pointer
    if not tree:
        return []
    cur = tree
    nodes = []
    inorder = []
    while cur or nodes:
        while cur:
            nodes.append(cur)
            cur = cur.left
        cur = nodes.pop()
        inorder.append(cur.data)
        cur = cur.right
    return inorder


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
