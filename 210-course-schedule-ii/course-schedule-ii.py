class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        stack = []
        state = [0]*numCourses
        def dfs(adj,node):
            if state[node] == 1 :
                return True
            if state[node] == 2 :
                return False
            state[node] = 1
            for i in adj[node] :
                if dfs(adj,i):
                    return True
            state[node] = 2
            stack.append(node)
        adj = [[] for _ in range(numCourses)]
        for u,v in prerequisites :
            adj[v].append(u)
        for i in range(numCourses):
            if state[i] == 0:
                if dfs(adj,i):
                    return []
        stack.reverse()
        return stack