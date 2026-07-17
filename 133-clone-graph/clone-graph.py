"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node :
            return 
        from collections import deque
        clones = {node : Node(node.val)}
        q = deque([node])
        while q :
            temp = q.popleft()
            for nei in temp.neighbors :
                if nei not in clones :
                    clones[nei] = Node(nei.val)
                    q.append(nei)
                clones[temp].neighbors.append(clones[nei])
        return clones[node]



        