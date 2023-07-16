class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        l=len(grades)
        c=0
        for i in range(1,len(grades)+1):
            if l-i>=0:
                c=c+1
                l=l-i
            else:
                return c
        return c
                