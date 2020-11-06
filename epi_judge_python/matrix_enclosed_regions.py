from typing import List

from test_framework import generic_test

from collections import deque
def fill_surrounded_regions(board: List[List[str]]) -> None:
    '''
    Constraints
        O: (Nothing to return, modify board in-place to flip surrounded white tiles)
        I: Board of B/W tiles, can be empty
    Ideas
        * any white tiles along border can't be flipped
         - do BFS from border, if we come across one, color it gray (G) so we know it's been visited, 
         adj white tiles will become gray too
            O(1) space
            O(n) time

    '''
    if not board or not board[0]:
            return
    top_border = [(0, j) for j in range(len(board[0])-1)]
    right_border = [(i,len(board[0])-1) for i in range(len(board)-1)]
    bot_border = [(len(board)-1, j) for j in reversed(range(1, len(board[0])))]
    left_border = [(i, 0) for i in reversed(range(1, len(board)))]
    q = deque(top_border + right_border + bot_border + left_border)

    while q:
        x, y = q.popleft()
        if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'W':
            board[x][y] = 'G'
            q.extend([(x+1,y), (x-1,y), (x,y+1), (x,y-1)])
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 'G':
                board[i][j] = 'B'
            else:
                board[i][j] = 'W'


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
