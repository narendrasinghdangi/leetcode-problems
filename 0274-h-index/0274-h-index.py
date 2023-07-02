class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations==[0] or citations==[0,0] or citations== [0,0,0]:
            return 0
        citations.sort()
        for i in range(len(citations),0,-1):
            h=i
            c=0
            j=len(citations)-1
            while citations[j]>=h and j>=0:
                c=c+1
                j=j-1
            if c>=h:
                return h
            