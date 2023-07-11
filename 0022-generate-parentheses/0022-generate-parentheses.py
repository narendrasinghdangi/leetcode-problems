class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        stack=[]
        def back(openN,closeN):
            if openN==closeN==n:
                ans.append("".join(stack))
                return
            if n>openN:
                stack.append("(")
                back(openN+1,closeN)
                stack.pop()
            if openN>closeN:
                stack.append(")")
                back(openN,closeN+1)
                stack.pop()
        back(0,0)
        return ans
                
                
                
        