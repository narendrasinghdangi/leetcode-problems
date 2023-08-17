class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        a=0
        for i in range(1,len(salary)-1):
            a=a+salary[i]
        return a/(len(salary)-2)