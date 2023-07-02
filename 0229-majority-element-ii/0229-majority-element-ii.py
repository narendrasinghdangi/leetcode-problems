class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        li=[]
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]=d[i]+1
        for i in d:
            if d[i]>len(nums)//3:
                li.append(i)
        return li