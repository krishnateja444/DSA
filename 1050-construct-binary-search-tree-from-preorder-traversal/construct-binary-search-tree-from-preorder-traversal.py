# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        for num in preorder[1:] :
            new = TreeNode(num)
            if stack[-1].val > num :
                stack[-1].left = new
            else :
                parent = None
                while stack and stack[-1].val < num :
                    parent = stack.pop()
                parent.right = new
            stack.append(new)
        return root


        
        


        