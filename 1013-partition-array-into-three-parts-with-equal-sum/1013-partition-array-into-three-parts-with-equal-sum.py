class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s=sum(arr)
        s=s/3
        su=0
        c=0
        i=0
        while len(arr)>i:
            su=su+arr[i]
            if su==s:
                c=c+1
                su=0
            i=i+1
            if c==2 and i<len(arr):
                if sum(arr[i:])==s:
                    return True
                else:
                    return False