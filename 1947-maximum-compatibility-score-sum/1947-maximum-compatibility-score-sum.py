class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
    
        def maxCompatibilityUtil(ssf,visited,res,idx):
            if idx==len(students):
                res[0] = max(res[0],ssf)
                return 

            for i in range(len(mentors)):
                if visited[i]==False:
                    visited[i]=True
                    temp = 0
                    for j in range(len(mentors[i])):
                        if mentors[i][j]==students[idx][j]:
                            temp = temp+1
                    maxCompatibilityUtil(ssf+temp,visited,res,idx+1)
                    visited[i]=False
        res = [-1]
        visited = [False]*len(students)
        maxCompatibilityUtil(0,visited,res,0)
        return res[0]