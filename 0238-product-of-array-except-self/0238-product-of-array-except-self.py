class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        for i in nums:
            p=p*i
        if p==0:
            li=[]
            for i in range(len(nums)):
                if nums[i]==0:
                    li.append(i)
                    p=1
                    for j in range(len(nums)):
                        if nums[j]!=0:
                            p=p*nums[j]
                    nums[i]=p
            if len(li)>=2:
                return [0]*len(nums)
            for i in range(len(nums)):
                if i!=li[0]:
                    nums[i]=0
            return nums
        for i in range(len(nums)):
            nums[i]=p//nums[i]
        return nums