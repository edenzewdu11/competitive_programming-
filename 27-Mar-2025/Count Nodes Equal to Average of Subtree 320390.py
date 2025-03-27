# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0  # Count of valid nodes

        def dfs(node):
            if not node:
                return (0, 0)  # Sum = 0, Count = 0
            
            l_sum, l_cnt = dfs(node.left)
            r_sum, r_cnt = dfs(node.right)

            s, c = l_sum + r_sum + node.val, l_cnt + r_cnt + 1

            if node.val == s // c:
                self.res += 1

            return (s, c)

        dfs(root)
        return self.res


        