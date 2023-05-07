class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lks=[]
        for i in range(len(obstacles)):
            x=obstacles[i]
            if len(lks)==0 or lks[-1]<=x:
                lks.append(x)
                obstacles[i]=len(lks)
            else:
                k=bisect_right(lks,x)
                lks[k]=x
                obstacles[i]=k+1
        return obstacles