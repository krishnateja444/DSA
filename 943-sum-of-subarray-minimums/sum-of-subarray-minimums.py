class Solution:
    def nse(self,arr):
        stack = []
        n = len(arr)
        ans = [n for i in range(n)]
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i] :
                ans[stack.pop()] = i
            stack.append(i)
        return ans
    def pse(self,arr):
        stack = []
        n = len(arr)
        ans = [-1 for i in range(n)]
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]] >= arr[i] :
                ans[stack.pop()] = i
            stack.append(i)
        return ans
    def sumSubarrayMins(self, arr: List[int]) -> int:
        r_sum = 0
        pse_r = self.pse(arr)
        nse_r = self.nse(arr)
        for i in range(len(arr)):
            left = i - pse_r[i]
            right = nse_r[i] - i
            r_sum += left * right * arr[i]
        return r_sum % (10**9 + 7)
