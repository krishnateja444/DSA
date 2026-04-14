class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        max_freq = 0
        count_max = 0
        for right in range(len(s)):
            if s[right] not in freq :
                freq[s[right]] = 1
            else :
                freq[s[right]] += 1
            max_freq = max(max_freq,freq[s[right]])
            size = right - left + 1
            while size - max_freq > k :
                freq[s[left]] -= 1
                #max_freq = max(freq.values())
                left += 1
                size = right - left + 1
            count_max = max(size,count_max)
        return count_max

        