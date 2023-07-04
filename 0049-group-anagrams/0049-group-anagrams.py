class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            lol="".join(sorted(i))
            if lol not in d:
                d[lol]=[i]
            else:
                d[lol].append(i)
        return list(d.values())