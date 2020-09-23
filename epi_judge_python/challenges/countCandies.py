'''
Return max product of 2 max nums from largest friend group(s)
https://repl.it/repls/UsableAttractiveWorkspace#main.py

# BRUTE FORCE
num friends ~ f
arr len ~ n
num weights ~ w
1. Build dict {weight: edge list}, O(n) time & O(n) space
 * While building, keep track of max edge length
{ 1: [[1, 2], [2, 3]]
  2: [[1, 2]
  3: [[2, 3], [2, 4]]}

  ***PROBLEM if for same weight, some edge(s) not connected

** ALTERNATE DICT ?
{1: {1: [2], 2: [3]},
 2: {1: [2]},
 3: {2: [3, 4]}}

2. Loop through keys to get list(s) with max edge length, O(w) * O(n) time
 * Put vertices into set to heapify (max_heap) and get max two nums
 * Keep track of max product

'''
def countCandies(friends_nodes, friends_from, friends_to, friends_weight):
    max_prod = 1
    n = len(friends_from)
    weights_edges = {}
    for i in range(n):
        if friends_weight[i] not in weights_edges:
            friends_weight[i] = []
        friends_weight[i].append([])
    

  return max_prod

friends_nodes = 4
friends_from = [1, 1, 2, 2, 2]
friends_to = [2, 2, 3, 3, 4]
friends_weight = [1, 2, 1, 3, 3]
print(countCandies(friends_nodes, friends_from, friends_to, friends_weight))
# -> 12