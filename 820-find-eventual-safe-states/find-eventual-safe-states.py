class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        stack = []
        n = len(graph)
        #safe = [False]*n
        state = [0]*n
        def dfs(adj,node):
            if state[node] == 1 :
                return True
            if state[node] == 2 :
                return False
            state[node] = 1
            for i in adj[node] :
                if dfs(adj,i) :
                    return True
            state[node] = 2
            #safe[node] = True
            return False
        visited = [False]*n
        for i in range(n):
            if state[i] == 0 :
                dfs(graph,i)
        for i in range(n) :
            if state[i] == 2 :
                stack.append(i)
        return stack
        