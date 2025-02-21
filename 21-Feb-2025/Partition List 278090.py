# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return None

        s_before = []
        s_after = []
        current = head
        
        while current:
            if current.val < x:
                s_before.append(current.val)
            current = current.next

        current = head
        while current:
            if current.val >= x:
                s_after.append(current.val)
            current = current.next
        
        s_before.extend(s_after)
        
        dummy = ListNode(-1)
        curr = dummy
        
        for num in s_before:
            curr.next = ListNode(num)
            curr = curr.next
        
        return dummy.next



        
        