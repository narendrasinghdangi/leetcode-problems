class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=0
        li=""
        for i in range(len(s)):
            li=s[i]
            for j in range(i+1,len(s)):
                if s[j] not in li:
                    li=li+s[j]
                else:
                    break
            if len(li)>m:
                m=len(li)
        return m
                