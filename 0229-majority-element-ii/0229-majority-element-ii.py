class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        li=[]
        d=Counter(nums)
        for i in d:
            if d[i]>len(nums)//3:
                li.append(i)
        return li