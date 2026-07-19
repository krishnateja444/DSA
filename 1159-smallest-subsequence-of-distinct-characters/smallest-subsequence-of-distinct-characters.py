class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        
        d = {}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        visited = set()
        for i in range(len(s)) :
            if s[i] in visited:
                d[s[i]] -= 1
                continue
            while stack and d[stack[-1]] > 0 and stack[-1] > s[i] :
                visited.remove(stack[-1])
                stack.pop()
            d[s[i]] -= 1
            if s[i] not in visited :
                stack.append(s[i])
                visited.add(s[i])
        return "".join(stack)
            

            
