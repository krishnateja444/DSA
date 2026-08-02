class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList :
            return 0
        from collections import deque
        q = deque()
        q.append((beginWord,1))
        while q :
            word,steps = q.popleft()
            if word == endWord :
                return steps
            word = list(word)
            for i in range(len(word)):
                org = word[i]
                for ch in "abcdefghijklmnopqrstuvwxyz" :
                    word[i] = ch
                    if ("".join(word)) in wordList :
                        q.append(("".join(word),steps + 1))
                        wordList.remove("".join(word))
                word[i] = org
        return 0
        
        
        
        