# URL: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []

        idx1, idx2 = 0, 0
        while idx1 < len(nums1) and idx2 < len(nums2):
            n1 = nums1[idx1]
            n2 = nums2[idx2]

            if n1 < n2:
                idx1 += 1
            elif n1 > n2:
                idx2 += 1
            else:
                ans.append(n1)
                idx1 += 1
                idx2 += 1
        
        return ans

#nums1, nums2 = [1,2,2,1], [2,2]     # output: [2, 2]
nums1, nums2 = [4,9,5], [9,4,9,8,4] # output: [4, 9]

test = Solution()

ans = test.intersect(nums1, nums2)
print(ans)
