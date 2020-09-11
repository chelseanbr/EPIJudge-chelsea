from typing import Set

from test_framework import generic_test

import collections
import string
def transform_string(D: Set[str], s: str, t: str) -> int:
    # O(l*d), where l is len of words, d is num of words in dict
    StringAndDistance = collections.namedtuple('StringAndDistance', ['string', 'distance'])
    # Do BFS with queue
    q = collections.deque([StringAndDistance(s, 0)])
    # Remove from dictionary to indicate seen
    D.remove(s)

    while q:
        curr_str = q.popleft()
        # Return steps to reach t once reached
        if curr_str.string == t:
            return curr_str.distance
        
        # Try all possibilities of changing 1 char in str
        for i in range(len(curr_str.string)):
            for char in string.ascii_lowercase: # Try chars a - z
                poss_next_str = curr_str.string[:i] + char + curr_str.string[i+1:] 
                if poss_next_str in D:
                    q.append(StringAndDistance(poss_next_str, curr_str.distance + 1))
                    D.remove(poss_next_str)
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
