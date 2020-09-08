from test_framework import generic_test


def square_root(k: int) -> int:
    l = 0
    r = k
    while l <= r:
        m = l + (r-l) // 2
        if m**2 > k:
            r = m-1
        else:
            l = m+1
    return l-1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
