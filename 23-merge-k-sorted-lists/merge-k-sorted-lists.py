# Definition for singly-linked list.
#class ListNode:
 #   def __init__(self, val=0, next=None):
  ##     self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #import heapq
        #heap = []
        l = []
        for node in lists :
            while node :
                #heapq.heappush(heap,node)
                l.append(node.val)
                node = node.next
        l.sort()
        if len(l) == 0 :
            return None

        curr = ListNode(0)
        head = curr
        prev = None
        for num in l :
            curr.val = num
            curr.next = ListNode(0)
            prev = curr
            curr = curr.next
        if prev :
            prev.next = None
        return head

        
        
        