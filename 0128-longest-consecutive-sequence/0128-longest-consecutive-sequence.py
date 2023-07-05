class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numsSet = set(nums)
        
        longestSeq = 0
        
        for each in nums:
            
            if each-1 not in numsSet:
                
                length = 0
                
                while(each+length in numsSet):
                    length+=1
                    
                longestSeq = max(length,longestSeq)
                
        return longestSeq   