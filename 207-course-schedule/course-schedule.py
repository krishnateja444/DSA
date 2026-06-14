class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def toposort(V,adj):
            indegree = [0]*V
            for i in range(V):
                for j in adj[i] :
                    indegree[j] += 1
            from collections import deque
            q = deque()
            for i in range(V):
                if indegree[i] == 0 :
                    q.append(i)
            topo = []
            while q :
                temp = q.popleft()
                for i in adj[temp]:
                    indegree[i] -= 1
                    if indegree[i] == 0 :
                        q.append(i)
                topo.append(temp)
            return topo
        adj = [[] for _ in range(numCourses)]
        for course,prereq in prerequisites :
            adj[prereq].append(course)
        topo = toposort(numCourses,adj)
        if len(topo) == numCourses :
            return True
        return False






        #adj = [[] for _ in range(numCourses)]
        #for course,prereq in prerequisites :
        #    adj[prereq].append(course)
       # state = [0]*(numCourses)
        #def iscycle(v):
        #    if state[v] == 1 :
         #       return True
         #   if state[v] == 2 :
        #        return False
        #    state[v] = 1
        #    for i in adj[v]:
        #        if iscycle(i):
           #        return True
           # state[v] = 2
            #return False
        
 
        for i in range(numCourses):
            if state[i] == 0 :
                if iscycle(i) :
                    return False
        return True



        