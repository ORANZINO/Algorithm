from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = int(1e5)

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit

"""
숫자를 진행시켜나가며 최저점을 갱신하고 그에 따른 최대수익을 계산하여 만약 기존의 수익보다 크다면 역시 갱신한다. 
"""
