class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums==[-1]:
            return ["-1"]
        res=[]
        li=[]
        for i in range(len(nums)-1):
            if (nums[i]+1)!=nums[i+1]:
                li.append(str(nums[i]))
                if len(li)!=1:
                    res.append(li[0]+"->"+li[-1])
                    li=[]
                else:
                    res.append(li[0])
                    li=[]
            else:
                li.append(str(nums[i]))
        if len(nums)<2:
            if len(nums)==0:
                return ""
            return str(nums[0])
        if (nums[-2]+1)!=nums[-1]:
            res.append(str(nums[-1]))
        else:
            res.append(li[0]+"->"+str(nums[-1]))
        return res