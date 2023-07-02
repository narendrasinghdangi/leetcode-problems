class Solution:
    def hIndex(self, cit: List[int]) -> int:
        
        l,r = 0, len(cit)
        
        while l<=r:
            mid = (l+r)>>1
            
            if cit[-mid]>=mid:
                l = mid+1
            else:
                r = mid-1
                
        return r