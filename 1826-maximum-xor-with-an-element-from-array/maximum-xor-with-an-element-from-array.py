class Trienode:
    def __init__(self):
        self.children = [None]*2
class Trie:
    def __init__(self):
        self.root = Trienode()
    def get_max(self,nums,q):
        nums.sort()
        q = [[i, num1, num2] for i, (num1, num2) in enumerate(q)]
        q.sort(key=lambda x:x[2])
        ans = [-1]*(len(q))
        j = 0
        for idx,num,l in q :
            while len(nums) > j and nums[j] <= l :
                curr = self.root
                for i in range(31,-1,-1):
                    bit = (nums[j] >> i)&1
                    if not curr.children[bit]:
                        curr.children[bit] = Trienode()
                    curr = curr.children[bit]
                j += 1
            if j == 0 :
                ans[idx] = -1
            else :
                ans[idx] = self.getmaxi(num)
        return ans
    def getmaxi(self,num):
        curr = self.root
        ans = 0
        for i in range(31,-1,-1):
            bit = (num >> i)&1
            if bit == 0 :
                if curr.children[1] :
                    curr = curr.children[1]
                    ans += 2**i
                else :
                    curr = curr.children[0]
            else :
                if curr.children[0] :
                    curr = curr.children[0]
                    ans += 2**i
                else :
                    curr = curr.children[1]
        return ans
            


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        trie = Trie()
        return trie.get_max(nums,queries)
        
        

        