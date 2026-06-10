class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        p1 = 0
        p2 = 0
        count = 0
        while True :
            if p1 >= len(g):
                break
            if p2 >= len(s):
                break
            if s[p2] >= g[p1]:
                count += 1
                p1 += 1
                p2 += 1
            else :
                p2 += 1
        return count
        