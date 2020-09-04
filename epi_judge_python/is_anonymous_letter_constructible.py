from test_framework import generic_test

import collections
def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    # O(1) space, O(n+m) time

    # Python reg dict
    chars = dict()
    for char in letter_text:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1
    
    for char in magazine_text:
        if char in chars:
            chars[char] -= 1
            if chars[char] == 0:
                del chars[char]
            if not chars:
                return True
    return not chars

    # Collections Counter
    # return (not collections.Counter(letter_text) - collections.Counter(magazine_text))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
