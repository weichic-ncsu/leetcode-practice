# URL: https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/

from typing import List

class Solution:
    def firstUniqChar(self, s: str) -> int:
        all_uniq_chars = {}

        for idx in range(len(s)):
            if s[idx] in all_uniq_chars:
                all_uniq_chars[s[idx]] = -1
            else:
                all_uniq_chars[s[idx]] = idx

        ans = len(s)
        for idx in all_uniq_chars.values():
            if not idx == -1 and idx < ans:
                ans = idx

        if ans == len(s):
            return -1
        else:
            return ans


#s = "leetcode"          # output: 0
s = "loveleetcode"      # output: 2
#s = "aabb"              # output: -1

test = Solution()

ans = test.firstUniqChar(s)
print(ans)
