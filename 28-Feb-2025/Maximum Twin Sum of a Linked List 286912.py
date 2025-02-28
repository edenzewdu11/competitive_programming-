# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        summ = 0
        max_sum = 0
        left=0
        right=len(arr)-1
        while left<right:
            summ=arr[left]+arr[right]
            max_sum=max(max_sum,summ)
            left+=1
            right-=1
        return max_sum
        

