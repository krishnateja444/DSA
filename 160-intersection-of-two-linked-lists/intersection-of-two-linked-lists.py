# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None :
            return None
        tempA = headA
        tempB = headB
        n1 = 0
        n2 = 0
        while True :
            if tempA != None :
                n1 += 1
                tempA = tempA.next
            if tempB != None :
                n2 += 1
                tempB = tempB.next
            if tempA == None and tempB == None :
                tempA = headA
                tempB = headB
                break
        if n1 > n2 :
            for _ in range(n1-n2):
                tempA = tempA.next
        elif n1 < n2 :
            for _ in range(n2 - n1):
                tempB = tempB.next
        if tempA == tempB :
            return tempA        
        while tempA != tempB and tempA != None and tempB != None:
            tempA = tempA.next
            tempB = tempB.next
        return tempA    



        


        