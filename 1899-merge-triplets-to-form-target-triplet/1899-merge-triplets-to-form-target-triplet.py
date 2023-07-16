class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        for i in range(3):
            j=0
            while len(triplets)>j:
                if target[i]<triplets[j][i]:
                    triplets.pop(j)
                    j=j-1
                j=j+1
        a = [x[0] for x in triplets]
        b = [x[1] for x in triplets]
        c = [x[2] for x in triplets]
        
        if target[0] not in a:
            return False
        if target[1] not in b:
            return False
        if target[2] not in c:
            return False
        return True