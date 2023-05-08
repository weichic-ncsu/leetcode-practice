class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        int buy_idx = 0, max_len = 0
        int profit = 0
        
        while buy_idx < len(prices) - 1:
            max_len = get_max_len_of_non_decending(prices[buy_idx + 1:], prices[buy_idx])
            profit += prices[buy_idx + max_len] - prices[buy_idx]
            buy_idx += 1
            
        return profit

    def get_max_len_of_non_decending(self, next_prices, buy_price):
        int len_of_non_decending_prices = 0

        while len_of_non_decending_prices < len(next_prices):
            if next_prices[len_of_non_decending_prices] < buy_price:
                return len_of_non_decending_prices
            else:
                len_of_non_decending_prices += 1
        
        return len_of_non_decending_prices