# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
      
        prev=None
        current=slow
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        
   
        while head and prev:
            if head.val!=prev.val:
                return False
            prev=prev.next
            head=head.next
        return True