class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            lol="".join(sorted(i))
            if lol not in d:
                d[lol]=[i]
            else:
                d[lol].append(i)
        li=[]
        for i in d:
            li.append(d[i])
        return li