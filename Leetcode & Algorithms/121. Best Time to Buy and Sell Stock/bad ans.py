class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = min(prices)
        min_index = prices.index(min_value)
        remove_prices = prices[min_index:]
        
        max_value = max(remove_prices)
        max_index = remove_prices.index(max_value)
        
        total = max_value - min_value
        return total
