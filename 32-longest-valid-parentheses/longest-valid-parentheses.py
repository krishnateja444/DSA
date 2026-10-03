class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l = 0
        r = 0
        maxi = 0

    # Left -> Right
        for ch in s:
            if ch == '(':
                l += 1
            else:
                r += 1

            if l == r:
                maxi = max(maxi, 2 * r)
            elif r > l:
                l = r = 0

    # Right -> Left
        s = s[::-1]
        l = 0
        r = 0

        for ch in s:
            if ch == '(':
                l += 1
            else:
                r += 1

            if l == r:
                maxi = max(maxi, 2 * l)
            elif l > r:
                l = r = 0

        return maxi