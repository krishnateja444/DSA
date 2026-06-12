# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #temp = -(2**31)
        l = []
        def inorder(node):
            if not node :
                return
            inorder(node.left)
            l.append(node.val)
            inorder(node.right)
        inorder(root)
        for i in range(1,len(l)):
            if l[i-1] >= l[i] :
                return False
        return True
