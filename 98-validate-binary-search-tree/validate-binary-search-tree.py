# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        temp = -(2**31) - 1
        #l = []
        def inorder(node):
            nonlocal temp
            if not node :
                return True
            if not inorder(node.left) :
                return False
            if temp >= node.val :
                return False
            temp = node.val
            return inorder(node.right)
        return inorder(root)
        #for i in range(1,len(l)):
        #    if l[i-1] >= l[i] :
        #        return False
        
