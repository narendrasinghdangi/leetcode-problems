class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        li = {}
        for i in cpdomains:
            count = int(i.split(" ")[0])
            s = (i.split(" ")[1]).split(".")
            lol = ""
            for j in range(len(s)-1, -1, -1):
                lol = s[j]+"."+lol
                if lol in li:
                    li[lol] = li[lol]+count
                else:
                    li[lol] = count
            print(li)
        list = []
        for i in li:
            lol = str(li[i])+" "+i[:-1]
            list.append(lol)


s = Solution()
s.subdomainVisits(["900 google.mail.com", "50 yahoo.com",
                  "1 intel.mail.com", "5 wiki.org"])
