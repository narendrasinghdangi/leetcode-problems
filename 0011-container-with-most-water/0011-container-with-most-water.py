class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        max_area=0
        while j>i:
            min_h=min(height[i],height[j])
            max_area=max(max_area,(j-i)*min_h)
            if height[i]>height[j]:
                j=j-1
            else:
                i=i+1
        return max_area