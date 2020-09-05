from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    cache = [1] + [0]*final_score
    for score in individual_play_scores:
        for i in range(score, len(cache)):
            cache[i] += cache[i-score]
    return cache[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
