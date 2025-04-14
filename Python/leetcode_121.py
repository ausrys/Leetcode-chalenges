'''
You are given an array prices where prices[i] is the price of a given stock
on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
'''
from typing import List


def max_profit(prices: List[int]) -> int:
    min_price = float('inf')
    max_pof = 0

    for price in prices:
        # Update the minimum price if a lower one is found
        if price < min_price:
            min_price = price
        # Calculate profit and update max_pof if it's better
        elif price - min_price > max_pof:
            max_pof = price - int(min_price)

    return max_pof


print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
print(max_profit([7, 6, 4, 3, 1]))  # 0
