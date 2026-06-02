class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res = []
        if len(digits) == 1 :
            return phone[digits[0]]
        def backtrack(i,s):
            if i == len(digits) :
                res.append(s[:])
                return
            for ch in phone[digits[i]] :
                backtrack(i + 1 , s + ch)
        backtrack(0,"")
        return res


        