# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node_val = []
        if not root :
            return 
        def inorder(root):
            if not root :
                return 
            inorder(root.left)
            node_val.append(root.val)
            inorder(root.right)
        inorder(root)
        return node_val[k-1]
            
        
        