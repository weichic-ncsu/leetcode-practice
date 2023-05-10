# URL: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/

from typing import List

class Solution:
    def get_max_len_of_non_decending(prices):
        idx = 0

        while idx < len(prices) - 1:
            if prices[idx + 1] < prices[idx]:
                return idx
            else:
                idx += 1

        return idx

    def maxProfit(self, prices: List[int]) -> int:
        buy_idx = 0
        max_len = 0
        profit = 0
        
        while buy_idx < len(prices) - 1:
            max_len = Solution.get_max_len_of_non_decending(prices[buy_idx:])
            profit += prices[buy_idx + max_len] - prices[buy_idx]
            buy_idx += (max_len + 1)

        return profit

#prices = [7,1,5,3,6,4]
#prices = [1,2,3,4,5]
prices = [7,6,4,3,1]

test = Solution()

ans = test.maxProfit(prices)
print(ans)
