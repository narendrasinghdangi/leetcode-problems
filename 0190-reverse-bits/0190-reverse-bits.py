class Solution:
    def reverseBits(self, n: int) -> int:
        b=bin(n)[2:][::-1]
        for i in range(32-len(b)):
            b=b+"0"
        return int(b,2)