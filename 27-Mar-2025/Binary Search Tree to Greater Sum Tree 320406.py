# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        curr = root
        stk = []
        
        while stk or curr:
            while curr:
                stk.append(curr)
                curr = curr.right
            
            curr = stk.pop()
            total += curr.val
            curr.val = total
            curr = curr.left
        
        return root
