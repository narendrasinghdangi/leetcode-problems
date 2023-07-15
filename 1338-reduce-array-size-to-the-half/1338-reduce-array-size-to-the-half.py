class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        l=len(arr)
        d=Counter(arr)
        d=dict(sorted(d.items(), key = lambda x :x[1],reverse=True))
        c=0
        nl=0
        for i in d:
            nl=nl+d[i]
            c=c+1
            if nl>=l//2:
                return c