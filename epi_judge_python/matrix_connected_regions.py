from typing import List

from test_framework import generic_test

from collections import deque
def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    '''
    1. edge case: if empty image, return
        - if not image or not image[0]
    2. get image dimensions
        - rowsize = len(image)
        - colsize = len(image[0])
    3. get bool at x, y
        - target_bool = image[x][y]
        - flipped_bool = not target_bool
        * flip initial pixel
    4. create & use queue
        - q = deque([(x, y)])
        cur_x, cur_y = q.popleft()
    5. evaluate each adjacent point
    #LEFT
    if 0 >= cur_x-1 < rowsize and image[cur_x-1][y] == target_bool: 
        # flip and add to queue
    #RIGHT
    #UP
    #DOWN
    * helper to check if flippable
    '''
    def is_flippable(x, y, image, target_bool):
        if 0 <= x < len(image) and 0 <= y < len(image[0]) \
            and image[x][y] == target_bool:
            return True
        else:
            return False
    if not image or not image[0]:
        return
    target_bool = image[x][y]
    q = deque([(x, y)])
    image[x][y] = not target_bool
    while q:
        cur_x, cur_y = q.popleft()
        for x, y in [(cur_x+1,cur_y),(cur_x-1,cur_y),(cur_x,cur_y+1),(cur_x,cur_y-1)]:
            if is_flippable(x, y, image, target_bool):
                q.append((x, y,))
                image[x][y] = not target_bool
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
