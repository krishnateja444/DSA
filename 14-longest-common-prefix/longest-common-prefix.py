class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j = 0
        if not strs or strs[0] == "":
            return ""
        if len(strs) == 1:
            return strs[0]
        while True:
            for i in range(len(strs)-1):
                if j >= len(strs[i]) or j >= len(strs[i+1]) or strs[i][j] != strs[i+1][j]:
                    return strs[0][:j]
            j += 1