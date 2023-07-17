class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d=Counter(tasks)
        c=0
        for i in d:
            if d[i]==1:
                return -1
            else:
                if d[i]%3==0:
                    c=c+d[i]//3
                else:
                    c=c+d[i]//3+1
        return c