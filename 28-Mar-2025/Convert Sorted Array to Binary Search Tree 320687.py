# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def balanced(l,r):
            if l>r:
                return None
            m=(l+r)//2
            root=TreeNode(nums[m])
            root.left=balanced(l,m-1)
            root.right=balanced(m+1,r)
            return root
        return balanced(0,len(nums)-1)