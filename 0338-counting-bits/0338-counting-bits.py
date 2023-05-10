class Solution:
    def countBits(self, n: int) -> List[int]:
        li=[]
        for i in range(n+1):
            b=bin(i)[2:]
            li.append(b.count("1"))
        return li


