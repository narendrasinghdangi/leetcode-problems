class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d={}
        nums.sort()
        for i in nums:
            if i%2==0:
                if i not in d:
                    d[i]=1
                else:
                    d[i]=d[i]+1
        if d=={}:
            return -1
        c=0
        e=0
        for i in d:
            if d[i]>c:
                c=d[i]
                e=i
        return e
                