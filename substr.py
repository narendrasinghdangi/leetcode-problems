class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        t = True
        while t:
            flag = False
            lol = ""
            for i in range(len(s)-len(part)+1):
                if part == s[i:i+len(part)]:
                    flag = True
                if flag:
                    lol = lol+s[i+len(part):]
                    break
                else:
                    lol = lol+s[i]
            if flag:
                flag = False
                s = lol
            else:
                t = False
            print(s)


s = Solution()
s.removeOccurrences("daabcbaabcbc", "abc")
