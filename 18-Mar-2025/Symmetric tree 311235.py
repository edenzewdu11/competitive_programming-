# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check_symmetry(obj,img):
            if not obj and not img :
                return True
            if (obj and not img ) or (not obj and img):
                return False
            if obj.val!=img.val:
                return False
            else:
                return check_symmetry(obj.right,img.left) and check_symmetry(obj.left,img.right)
        return check_symmetry(root,root)


      

        