class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans=[0,0,0]
        for i in triplets:
            if i[0]>target[0] or i[1]>target[1] or i[2]>target[2]:
                continue
            for k in range(len(target)):
                if i[k]==target[k]:
                    ans[k]=1
        if sum(ans)==3:
            return True
        else:
            return False