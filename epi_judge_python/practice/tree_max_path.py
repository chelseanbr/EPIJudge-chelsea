'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/
https://leetcode.com/problems/binary-tree-maximum-path-sum/

      10
     /  \
   11    7
   /    / \
  3    1   5
 / \
2   4

BFS: [10, 11, 7, 3, null, 1, 5, 2, 4, null, null, null, null, null, null]
--> 4
--> [10->11->3->2]
'''
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def maxDepth(root):
#     if not root:
#         return 0
#     max_depth = 0
#     # Traverse through tree and keep track of cur depth, max depth
#     # Either DFS or BFS works, will do DFS iteratively with stack
#     nodes_depths = [(root, 1)]
#     while nodes_depths:
#         node, depth = nodes_depths.pop()
#         max_depth = max(max_depth, depth)
#         if node.left:
#             nodes_depths.append((node.left, depth+1))
#         if node.right:
#             nodes_depths.append((node.right, depth+1))
#     return max_depth

# RECURSIVE
def maxDepth(root: TreeNode) -> int:
    if not root:    # if the tree is empty
        return 0
    elif not (root.left or root.right): # if the tree only has its root (this is the base case)
        return 1
    else:      # everytime the function calls itself and  the depth increases by 1
        return max(maxDepth(root.left),maxDepth(root.right))+1

def maxPath(root: TreeNode) -> int:
    def maxPath_helper(root, max_path, max_path_len):
        left = maxPath_helper(root.left, max_path, max_path_len)
        right = maxPath_helper(root.right, max_path, max_path_len)

        if not root:
            return max_path
        else:
            max_path.append(root.val)

        return max_path

    if not root:    # if the tree is empty
        return []
    return maxPath_helper(root, [root.val], 1)

def bfs_iterative(root):
    if not root:
        return []
    traversal = []
    q = deque([root])
    while q:
        node = q.popleft()
        if not node:
            traversal.append('null')
        else:
            traversal.append(node.val)
            q.append(node.left)
            q.append(node.right)
    return traversal



root = TreeNode(10)
lvl2_node1 = TreeNode(11)
lvl2_node2 = TreeNode(7)
root.left = lvl2_node1
root.right = lvl2_node2
lvl3_node1 = TreeNode(3)
lvl2_node1.left = lvl3_node1
lvl3_node2 = TreeNode(1)
lvl3_node3 = TreeNode(5)
lvl2_node2.left = lvl3_node2
lvl2_node2.right = lvl3_node3
lvl4_node1 = TreeNode(2)
lvl4_node2 = TreeNode(4)
lvl3_node1.left = lvl4_node1
lvl3_node1.right = lvl4_node2
# print(bfs_iterative(root))
print(maxDepth(root))
print(maxPath(root))