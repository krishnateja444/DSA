# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sym(root1,root2):
            if not (root1 or root2 ) :
                return True
            if not root1 :
                return False
            if not root2 :
                return False
            if root1.val != root2.val :
                return False
            if sym(root1.left,root2.right) and sym(root1.right,root2.left) :
                return True
            return False
            
        if not root.left :
            if root.right :
                return False
            else :
                return True
        if not root.right :
            if root.left :
                return False
        return sym(root.left,root.right)
            


        