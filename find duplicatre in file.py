class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        l1 = []
        l2 = []
        for i in paths:
            print(i)


s = Solution()
s.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)",
                "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
