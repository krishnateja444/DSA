class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = [i for i in range(n)]
        rank = [0]*(n)
        def findpar(node):
            if node == parent[node]:
                return node
            parent[node] = findpar(parent[node])
            return parent[node] 
        def unionbyrank(u,v):
            ultp_u = findpar(u)
            ultp_v = findpar(v)
            if ultp_u == ultp_v :
                return 
            if rank[ultp_u] < rank[ultp_v] :
                parent[ultp_u] = ultp_v
            elif rank[ultp_u] > rank[ultp_v]:
                parent[ultp_v] = ultp_u
            else :
                parent[ultp_u] = ultp_v
                rank[ultp_v] += 1
        for i in range(n):
            for j in range(i+1,n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    unionbyrank(i,j)
        comp = 0
        for i in range(n):
            if parent[i] == i :
                comp += 1
        return n - comp