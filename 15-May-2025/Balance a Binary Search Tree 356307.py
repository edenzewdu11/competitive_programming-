# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
       
        def inorder(n):
            return inorder(n.left) + [n.val] + inorder(n.right) if n else []
        
        def build(arr):
            if not arr: return None
            m = len(arr) // 2
            n = TreeNode(arr[m])
            n.left = build(arr[:m])
            n.right = build(arr[m+1:])
            return n

        return build(inorder(root))

            