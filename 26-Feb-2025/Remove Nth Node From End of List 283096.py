# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        for _ in range(n - 1):
            curr = curr.next
        curr.next = curr.next.next if curr.next else None

        prev = None
        curr = dummy.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev



        
        