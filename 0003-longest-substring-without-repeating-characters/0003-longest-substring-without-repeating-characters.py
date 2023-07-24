class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m=0
        li=[]
        i=0
        while len(s)>i:
            if s[i] in li:
                m=max(m,len(li))
                i=i-len(li)
                li=[]
            else:
                li.append(s[i])
            i=i+1
        m=max(m,len(li))
        return m