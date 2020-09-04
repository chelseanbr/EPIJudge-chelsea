from test_framework import generic_test


def gcd(x: int, y: int) -> int:
    # Recursive: O(n) space, O(n) time
    # return x if y == 0 else gcd(y, x % y)

    # Iterative: O(1) space, O(n) time
    while y != 0:
        result = x % y
        x = y
        y = result
    return x

if __name__ == '__main__':
    exit(generic_test.generic_test_main('euclidean_gcd.py', 'gcd.tsv', gcd))
