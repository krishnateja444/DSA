# Definition for singly-linked list.

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None :
            return head
        curr = head
        l = []
        while curr :
            l.append(curr.val)
            curr = curr.next
        l.sort()
        head = ListNode(l[0])
        temp = head
        for i in range(1,len(l)):
            temp.next = ListNode(l[i])
            temp = temp.next
        return head
