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
        def pre_order(root):
            if not root :
                return 
            node_val.append(root.val)
            pre_order(root.left)
            pre_order(root.right)
        pre_order(root)
        node_val.sort()

        return node_val[k-1]
            
        
        