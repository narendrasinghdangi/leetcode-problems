class Solution:
    def numTeams(self, rating: List[int]) -> int:
        greater = defaultdict(int)
        lesser = defaultdict(int)
        print(greater)
        for i in range(len(rating)-1):
            for j in range(i+1, len(rating)):
                if rating[i] < rating[j]:
                    greater[i] += 1
                else:
                    lesser[i] += 1
        ans = 0
        print(greater, lesser)
        for i in range(len(rating)-2):
            for j in range(i+1, len(rating)):
                if rating[i] < rating[j]:
                    ans+=greater[j]
                else:
                    ans+=lesser[j]
        return ans