class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        e=[0]
        o=[0]
        for i in range(len(nums)):
            if i%2==0:
                e.append(e[-1]+nums[i])
                o.append(o[-1])
            else:
                o.append(o[-1]+nums[i])
                e.append(e[-1])
        c=0
        for i in range(1,len(nums)+1):
            ee=e[-1]-e[i]+o[i-1]
            oo=o[-1]-o[i]+e[i-1]
            if ee==oo:
                c=c+1
        return c
            
                    