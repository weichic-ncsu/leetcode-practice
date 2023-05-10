# URL: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for idx in range(int(len(s)/2)):
            s[idx], s[-1-idx] = s[-1-idx], s[idx]


#s = ["h","e","l","l","o"]       # output: ["o","l","l","e","h"]
s = ["H","a","n","n","a","h"]   # output: ["h","a","n","n","a","H"]

test = Solution()

test.reverseString(s)
print(s)
