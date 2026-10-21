class Solution:
    def minOperations(self, s: str) -> int:
        l = list(s)
        req = sorted(l)
        if l == req :
            return 0
        mini = min(l)
        mini_i = l.index(mini)
        maxi = max(l)
        if mini_i != len(s) - 1 and mini_i != 0 :
            l[:-1] = sorted(l[:-1])
            if l == req :
                return 1
            return 2
        elif mini_i == 0 :
            return 1
        else :
            if len(l) == 2 :
                return -1
            l[1:] = sorted(l[1:])
            if maxi == l[-1] :
                return 2
            return 3
            
        