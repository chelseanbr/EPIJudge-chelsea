from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    # O(n) time, O(h) space, iterative
    def inOrder(root, k): 
      
        # Set current to root of binary tree 
        current = root  
        stack = [] # initialize stack 
        done = 0 
        
        while True: 
            
            # Reach the left most Node of the current Node 
            if current is not None: 
                
                # Place pointer to a tree node on the stack  
                # before traversing the node's left subtree 
                stack.append(current) 
            
                current = current.left  
    
            
            # BackTrack from the empty subtree and visit the Node 
            # at the top of the stack; however, if the stack is  
            # empty you are done 
            elif(stack): 
                current = stack.pop() 
                # print(current.data, end=" ") # Python 3 printing 
                if current.data > k:
                    return current
            
                # We have visited the node and its left  
                # subtree. Now, it's right subtree's turn 
                current = current.right  
    
            else: 
                break
    return inOrder(tree, k)

    # O(n) time, O(h) space, recursive ?
    


    # # O(h) time, O(1) space
    # subtree = tree
    # result = None
    # while subtree:
    #     if subtree.data <= k:
    #         subtree = subtree.right
    #     else:
    #         result = subtree
    #         subtree = subtree.left
    # return result


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
