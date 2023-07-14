class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = ""
        stack = []
        for i in range(len(pattern)+1): 
            stack.append(str(i+1))
            if i == len(pattern) or pattern[i] == 'I': 
                while stack:
                    ans=ans+stack.pop()
        return ans 