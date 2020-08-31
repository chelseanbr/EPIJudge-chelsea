from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_profit = 0.0
    # O(n^2) time, O(1) space - TOO SLOW!
    # for i in range(len(prices)):
    #     for j in range(i+1, len(prices)):
    #         max_profit = max(max_profit, prices[j]-prices[i])

    # O(n^2) time, O(1) space
    if len(prices) >= 2:
        min_buy = prices[0]
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_buy)
            min_buy = min(min_buy, price)
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
