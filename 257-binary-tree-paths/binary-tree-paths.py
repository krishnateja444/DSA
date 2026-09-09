# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(node,arr):
            if not node :
                return False
            arr.append(node.val)
            if not node.left and not node.right:
                ans.append("->".join(map(str,arr)))
            dfs(node.left,arr)
            dfs(node.right,arr)
            arr.pop()
        dfs(root,[])
        return ans

        