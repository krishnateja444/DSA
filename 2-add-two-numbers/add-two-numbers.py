# Definition for singly-linked list.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = l1 
        s2 = l2
        s3 = ListNode(0)
        head = s3
        c = 0
        prev = None
        while s1 != None or s2 != None :
            prev = s3
            if s1 == None :
                s3.val = s2.val + c  
                s2 = s2.next
            elif s2 == None :
                s3.val = s1.val + c
                s1 = s1.next
            else :
                s3.val = s1.val + s2.val + c
                s1 = s1.next
                s2 = s2.next
            c = 0    
            if s3.val >= 10 :
                s3.val = s3.val - 10
                c = 1
            s3.next = ListNode(0)
            s3 = s3.next    
            
        if c == 1 :
            s3.val = 1
        else:
            prev.next = None
        return head             
           