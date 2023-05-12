# URL: https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/

from typing import Optional
from TreeNode import TreeNode, generate_treenode, print_tree_node

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


root = [3,9,20,None,None,15,7]      # output: 3
#root = [1,None,2]                   # output: 2
#root = []

tree_node = generate_treenode(root)
#print_tree_node(tree_node)

test = Solution()
ans = test.maxDepth(tree_node)
print(ans)
