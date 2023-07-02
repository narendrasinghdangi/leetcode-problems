class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=""
        l=201
        for i in strs:
            l=min(len(i),l)
        for i in range(l):
            for j in range(len(strs)-1):
                if strs[j][i]!=strs[j+1][i]:
                    return s
            s=s+strs[0][i]
        return s