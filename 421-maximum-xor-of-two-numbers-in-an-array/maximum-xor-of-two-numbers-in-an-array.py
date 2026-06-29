class Trienode:
    def __init__(self):
        self.children = {}
        self.isend = False

class Trie :
    def __init__(self):
        self.root = Trienode()
    def insert(self,word):
        curr = self.root
        for ch in word:
            if ch not in curr.children :
                curr.children[ch] = Trienode()
            curr = curr.children[ch]
        curr.isend = True
    def search(self,word):
        curr = self.root
        for ch in word :
            if ch not in curr.children :
                return False
            curr = curr.children[ch]
        return curr.isend
    def dectobin(self,x):
        l = []
        if x == 0 :
            return '0'*(32)
        while x > 0 :
            l.append(str(x%2))
            x = x//2
        ans = "".join(l[::-1])
        n = len(ans)
        ans = "0"*(32-n) + ans
        return ans
    def getmax(self,arr1,arr2):
        for num in arr1 :
            word = self.dectobin(num)
            self.insert(word)
        maxi = float('-inf')
        for num in arr2 :
            maxi = max(maxi,self.getmaxi(num))
        return maxi
    def getmaxi(self,x):
        st = self.dectobin(x)
        curr = self.root
        ans = ""
        for ch in st:
            if ch == '0' :
                if '1' in curr.children :
                    curr = curr.children['1']
                    ans = ans + '1'
                else :
                    curr = curr.children['0']
                    ans = ans + '0'
            else:
                if '0' in curr.children :
                    curr = curr.children['0']
                    ans = ans + '0'
                else :
                    curr = curr.children['1']
                    ans = ans + '1'
        ans = int(ans,2)
        return ans^(x)

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        return trie.getmax(nums,nums)

        