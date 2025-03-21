# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        left_child = root.left
        right_child = root.right
        
        def reverse_nodes(left_child, right_child, level):
            if left_child:
                if level % 2 != 0:
                    left_child.val, right_child.val = right_child.val, left_child.val
                level += 1
                reverse_nodes(left_child.left, right_child.right, level)
                reverse_nodes(left_child.right, right_child.left, level)
            return
        
        reverse_nodes(left_child, right_child, 1)
        return root
