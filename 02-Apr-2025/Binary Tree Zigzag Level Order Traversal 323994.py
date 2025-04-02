# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        def max_depth(curr, level=1):
            if not curr:
                return
            result.append((level, curr.val))
            if curr.left:
                max_depth(curr.left, level + 1)
            if curr.right:
                max_depth(curr.right, level + 1)
        
        max_depth(root)
        
        dictt = defaultdict(list)
        for level, val in result:
            dictt[level].append(val)
        
        answer = []
        for level in sorted(dictt.keys()):
            if level % 2 == 0:
                answer.append(dictt[level][::-1])
            else:
                answer.append(dictt[level])
        
        return answer


            
            
            