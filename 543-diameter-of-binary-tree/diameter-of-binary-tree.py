# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        if not (root.left or root.right) :
            return 0
        def height(root):
            if not root :
                return 0
            left = height(root.left)
            right = height(root.right)
            self.diameter = max(self.diameter,left + right)
            return 1 + max(left,right)
        height(root)
        return self.diameter
    
        
        