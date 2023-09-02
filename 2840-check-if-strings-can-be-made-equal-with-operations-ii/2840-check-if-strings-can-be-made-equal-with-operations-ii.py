from collections import Counter
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1e={}
        s2e={}
        s1o={}
        s2o={}
        for i in range(len(s1)):
            if i%2==0:
                s1e[s1[i]]=s1e.get(s1[i],0)+1
                s2e[s2[i]]=s2e.get(s2[i],0)+1
            else:
                s1o[s1[i]]=s1o.get(s1[i],0)+1
                s2o[s2[i]]=s2o.get(s2[i],0)+1
        return s1e==s2e and s1o==s2o