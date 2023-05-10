# URL: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
#
# Constraints:
#   1. 1 <= nums.length <= 3 * 104
#   2. -3 * 104 <= nums[i] <= 3 * 104
#   3. Each element in the array appears twice except for one element which appears only once.

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        all_nums = {}

        for num in nums:
            if num in all_nums:
                all_nums.pop(num)
            else:
                all_nums[num] = 1

        return list(all_nums.keys())[0]


#nums = [2,2,1]      # output: 1
#nums = [4,1,2,1,2]  # output: 4
nums = [1]          # output: 1

test = Solution()

ans = test.singleNumber(nums)
print(ans)
