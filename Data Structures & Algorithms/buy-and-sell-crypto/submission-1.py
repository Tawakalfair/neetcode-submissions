class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_price = 0
        for x in prices:
            if x < min_price:
                min_price = x
            elif x - min_price > max_price:
                max_price = x - min_price
        
        return max_price