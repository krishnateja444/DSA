# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True
        def check(p,q):
            if not (p or q) :
                return True
            if ((not p) and q ) or ((not q) and p) :
                return False
            if p.val != q.val :
                return False
            if not (check(p.left,q.left) and check(p.right,q.right)) :
                return False
            return True
        return check(p,q)      
        