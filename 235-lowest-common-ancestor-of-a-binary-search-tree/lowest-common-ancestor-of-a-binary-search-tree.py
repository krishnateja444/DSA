# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val :
            p,q = q,p
        def lca(node,p,q):
            if p.val <= node.val <= q.val :
                return node
            else :
                if (q.val < node.val ) :
                    return lca(node.left,p,q)
                else :
                    return lca(node.right,p,q)
        return lca(root,p,q)


        
        