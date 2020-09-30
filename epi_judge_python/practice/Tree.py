'''
Every tree has a trunk
From a trunk there's 0 or more branches


function
O: len of longest path to bush
I: Tree
C: O(n) time  __
E: 

APPROACH #1:
DFS or BFS
backtracking since could end up at null end


'''
from collections import deque
class Tree:
    def __init__(self, trunk_length):
        self.trunk_length = 10
        self.trunk_end = # can be other branch(es) in a list or null or bush
        
class Branch:
    def __init__(self):
        self.start # can be trunk or another branch or 
        self.end # can be other branch(es) in a list or null or bush
        self.length
    
class Bush:
    def __init__(self):
        self.length = 0
        
        
def max_path_to_bush(tree):
    if not tree.trunk_end: #Null
        return 0
    if instance_of(tree.trunk_end, Bush): # check is bush
        return tree.trunk_length
    max_path_len = tree.trunk_length
    
    # for example: [b1, b2, b3]
    # Use queue to do BFS
    q = deque([])
    for branch in tree.trunk_end:
        q.append(branch)
        
    while q: # not empty
    # for example: [b1, b2, b3]
        cur = q.popleft() #b1
        # Branch ends in bush
        
        # Branch ends in nothing
        
        # Branch splits off
    
    return max_path_len