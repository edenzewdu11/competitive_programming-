# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        g_prev = dummy

        while True:
            kthNode = self.getkthNode(g_prev, k)
            if kthNode is None:
                break
            g_next = kthNode.next

            prev = kthNode.next
            current = g_prev.next
            while current != g_next:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
           
            temp = g_prev.next
            g_prev.next = kthNode
            g_prev = temp
        return dummy.next

    def getkthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

        
       





