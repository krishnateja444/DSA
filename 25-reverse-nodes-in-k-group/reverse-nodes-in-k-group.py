# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        while True:
            kth = prev_group
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            next_group = kth.next
            prev = next_group
            curr = prev_group.next
            while curr != next_group:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp
