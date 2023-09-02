from collections import Counter
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1e={}
        s2e={}
        s1o={}
        s2o={}
        for i in range(len(s1)):
            if i%2==0:
                if s1[i] in s1e:
                    s1e[s1[i]]=s1e[s1[i]]+1
                else:
                    s1e[s1[i]]=1
                if s2[i] in s2e:
                    s2e[s2[i]]=s2e[s2[i]]+1
                else:
                    s2e[s2[i]]=1
            else:
                if s1[i] in s1o:
                    s1o[s1[i]]=s1o[s1[i]]+1
                else:
                    s1o[s1[i]]=1
                if s2[i] in s2o:
                    s2o[s2[i]]=s2o[s2[i]]+1
                else:
                    s2o[s2[i]]=1
        return s1e==s2e and s1o==s2o
            