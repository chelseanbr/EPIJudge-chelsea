from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    if len(square_matrix)<1:
        return []

    m = len(square_matrix)
    n = len(square_matrix[0])
    result = []

    top_row = 0 
    bot_row = m - 1
    left_col = 0 
    right_col = n - 1
    while top_row <= bot_row and left_col <= right_col:
        # 1. go across top row, left to right
        for i in range(left_col, right_col + 1):
            result.append(square_matrix[top_row][i])
        top_row += 1
        # 2. go down right col, top to bot
        for i in range(top_row, bot_row + 1):
            result.append(square_matrix[i][right_col])
        right_col -= 1
        if top_row <= bot_row:
            # 3. go across bot row, right to left (reversed)
            for i in range(right_col, left_col - 1, -1):
                result.append(square_matrix[bot_row][i])
            bot_row -= 1
        if left_col <= right_col:
            # 4. go up left col, bot to top (reversed)
            for i in range(bot_row, top_row - 1, -1):
                result.append(square_matrix[i][left_col])
            left_col += 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
