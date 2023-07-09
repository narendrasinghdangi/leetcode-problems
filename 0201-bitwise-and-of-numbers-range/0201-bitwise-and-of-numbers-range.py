class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        summ = right

        while(right > left):
            summ = right & (right-1)
            right = summ
        return summ