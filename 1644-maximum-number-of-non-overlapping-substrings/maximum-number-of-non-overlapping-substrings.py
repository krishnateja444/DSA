class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        start = {}
        last = {}
        for i in range(len(s)) :
            ch = s[i]
            if ch not in start :
                start[ch] = i
                last[ch] = i
            else :
                last[ch] = i
        intervals = []
        for ch in set(s) :
            p = True
            r = last[ch]
            l = start[ch]
            while l <= r :
                r = max(r,last[s[l]])
                l += 1
            for i in range(start[ch],r+1):
                if start[ch] > start[s[i]] :
                    p = False
                    break
            if p :
                intervals.append([start[ch],r])
        print(intervals)
        intervals.sort()
        last_interval = intervals[0][1]
        ans = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0] > last_interval :
                ans.append(intervals[i])
                last_interval = intervals[i][1]
            else :
                if last_interval >= intervals[i][1] :
                    ans.pop()
                    ans.append(intervals[i])
                    last_interval = intervals[i][1]
        res = []
        for start,end in ans :
            res.append(s[start:end+1])
        return res
                    

        

