class Solution:
    def candy(self, ratings: List[int]) -> int:
        l=len(ratings)
        c=[1]*l
        for i in range(1,l):
            if ratings[i]>ratings[i-1]:
                c[i] = c[i-1] + 1
        for i in range(l - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and c[i] <= c[i+1]:
                c[i] = c[i+1] + 1
        return sum(c)