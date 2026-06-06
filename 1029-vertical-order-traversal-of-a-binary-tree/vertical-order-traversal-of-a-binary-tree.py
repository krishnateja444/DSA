# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def dfs(node,row,col):
            if not node :
                return
            ans.append((col,row,node.val))
            dfs(node.left,row + 1 , col - 1)
            dfs(node.right,row + 1, col + 1)
        dfs(root,0,0)
        ans.sort()
        res = []
        ## res list formation
        prev_col = None
        for col,row,val in ans :
            if col != prev_col :
                res.append([])
                prev_col = col
            res[-1].append(val)
        return res

        



        


        