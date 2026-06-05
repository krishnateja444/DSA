# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height = 0
        def max_height(root):
            if not root :
                return 0
            return 1 + max(max_height(root.left),max_height(root.right))

        height = max_height(root)
        return height

        