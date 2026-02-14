class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for ch in s :
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

        sorted_items = sorted(d.items(),key=lambda x: x[1] , reverse = True)
        result = ""
        for char,count in sorted_items :
            result += char * count
        return result
    

        


        