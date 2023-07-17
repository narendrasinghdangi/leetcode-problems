class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=0
        arr = [0]*len(nums)
        while nums[:]!=arr[:]:
            even=True
            for i in range(len(nums)):
                if nums[i]%2!=0:
                    nums[i]=nums[i]-1
                    c=c+1
                    even=False
            if even:
                nums=[j/2 for j in nums]
                c=c+1
        return c
    
                
                