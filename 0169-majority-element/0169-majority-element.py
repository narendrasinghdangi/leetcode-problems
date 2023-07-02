class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        c=0
        e=0
        for i in d:
            if d[i]>c:
                c=d[i]
                e=i
        return e