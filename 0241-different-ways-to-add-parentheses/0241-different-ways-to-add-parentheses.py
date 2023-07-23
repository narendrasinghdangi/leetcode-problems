class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        dp={}
        def solve(exp):
            if exp.isdigit():
                return [int(exp)]
            if exp in dp:
                return dp[exp]
            res=[]
            for i in range(len(exp)):
                if exp[i] in "+-*":
                    l=solve(exp[:i])
                    r=solve(exp[i+1:])
                    for a in l:
                        for b in r:
                            if exp[i]=="+":
                                res.append(a+b)
                            elif exp[i]=="-":
                                res.append(a-b)
                            else:
                                res.append(a*b)
            dp[exp]=res
           
            return dp[exp]
        return solve(expression)