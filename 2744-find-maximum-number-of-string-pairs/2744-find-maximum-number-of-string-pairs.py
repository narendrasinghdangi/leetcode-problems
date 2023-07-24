class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        c=0
        words=list(set(words))
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i]==words[j][::-1]:
                    c=c+1
        return c