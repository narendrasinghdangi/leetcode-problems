class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s=s+str(i)
        s=int(s)+1
        li=[]
        for i in str(s):
            li.append(int(i))
        return li