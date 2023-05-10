# URL: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
#
# Constraints: 
#   1. 1 <= nums.length <= 105
#   2. -231 <= nums[i] <= 231 - 1
#   3. 0 <= k <= 105
#
# Follow up:
#   1. Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
#   2. Could you do it in-place with O(1) extra space?

from typing import List

class Solution:
    def new_rotate(nums, k):
        k = k % len(nums)
        if k > 0:
            if len(nums) == 2:
                nums[0], nums[1] = nums[1], nums[0]
            elif k > len(nums)/2:
                k -= len(nums)
                nums[: -k], nums[k: ] = nums[k: ], nums[: -k]
                nums[: k] = Solution.new_rotate(nums[: k], k)
            else:
                nums[: k], nums[-k: ] = nums[-k: ], nums[: k]
                nums[k: ] = Solution.new_rotate(nums[k: ], k)
        return nums

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        if k > 0:
        
        # 1. Use a new array
        #    temp = nums[-k: ]
        #    nums[-len(nums[: -k]): ] = nums[: -k]
        #    nums[: k] = temp

        # 2. 
        #    tmp = Solution.new_rotate(nums, k)
        #    nums[:] = tmp[:]

        # 3.
            


nums, k = [1,2,3,4,5,6,7], 3        # output: [5,6,7,1,2,3,4]
#nums, k = [-1,-100,3,99], 2         # output: [3,99,-1,-100]

test = Solution()

test.rotate(nums, k)
print(nums)

#[1, 2, 3, 4, 5, 6, 7], 3 --> [5, 6, 7] + [4, 1, 2, 3], 3 --> [5, 6, 7] + [3, 1, 2], -1 + [4] --> [5, 6, 7] + [3, 1, 2], 2 + [4]
#--> [5, 6, 7] + [2, 1], -1 + [3, 4] --> [5, 6, 7, 1, 2, 3, 4]
#[1, 2, 3, 4, 5, 6, 7], 2 --> [6, 7] + [3, 4, 5, 1, 2], 2 --> [6, 7, 1, 2] + [5, 3, 4], 2 --> [6, 7, 1, 2] + [5, 3, 4], -1 --> [6, 7, 1, 2] + [4, 3], -1 + [5]
#--> [6, 7, 1, 2] + [4, 3], 1 + [5] --> [6, 7, 1, 2, 3, 4, 5]
#[1, 2, 3, 4, 5, 6, 7], 4 --> [1, 2, 3, 4, 5, 6, 7], -3 --> [5, 6, 7, 4], -3 + [1, 2, 3] --> [5, 6, 7, 4], 1 + [1, 2, 3] --> [4] + [6, 7, 5], 1 + [1, 2, 3]
#--> [4, 5] + [7, 6], 1 + [1, 2, 3] --> [4, 5, 6, 7, 1, 2, 3]
#
#
#[1, 2, 3, 4], 1 --> [4] + [2, 3, 1], 1 --> [4, 1] + [3, 2], 1 --> [4, 1, 2, 3]
#[1, 2, 3, 4], 2 --> [3, 4] + [1, 2], 2 --> [3, 4] + [1, 2], 0 --> [3, 4, 1, 2]
#[1, 2, 3, 4], 3 --> [1, 2, 3, 4], -1 --> [4, 2, 3], -1 + [1] --> [4, 2, 3], 2 + [1] --> [4, 2, 3], -1 + [1] --> [3, 2], -1 + [4, 1]
#--> [3, 2], 1 + [4, 1] --> [2, 3, 4, 1]
