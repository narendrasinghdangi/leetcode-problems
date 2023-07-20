class Solution:
    def numTeams(self, rating: List[int]) -> int:
        upper_dps = [0]*len(rating)
        lower_dps = [0]*len(rating)
        c=0
        for i in range(len(rating)):
            for j in range(i):
                if rating[j] < rating[i]:
                    c += upper_dps[j]
                    upper_dps[i] += 1
                else:
                    c += lower_dps[j]
                    lower_dps[i] += 1
        return c