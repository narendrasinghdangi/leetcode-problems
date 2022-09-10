class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                l.append(i)
            else:
                if len(l) >= 1 and i == ")" and l[-1] == "(":
                    l.pop()
                elif len(l) >= 1 and i == "}" and l[-1] == "{":
                    l.pop()
                elif len(l) >= 1 and i == "]" and l[-1] == "[":
                    l.pop()
                else:
                    print("false")
        if len(l) == 0:
            print("yes", l)
        print(l)


s = Solution()
s.isValid("()")
