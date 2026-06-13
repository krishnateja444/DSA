# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        def insert(root,val):
            if not root :
                return TreeNode(val)
            if root.val > val :
                root.left = insert(root.left,val)
            elif root.val < val :
                root.right = insert(root.right,val)
            return root
        for num in preorder :
            insert(root,num)
        return root

    

        



            

        
        


        