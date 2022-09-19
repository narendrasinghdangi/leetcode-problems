class Solution:
    def findOriginalArray(self, changed: list[int]) -> list[int]:
        changed.sort()
        if changed[0]==0:
            return []
        li = []
        for i in range(len(changed)//2):
            lol = changed[i]
            if (2*lol) in changed:
                li.append(lol)
                changed.remove(2*lol)
            else:
                print([])
        print(li)


s = Solution()
s.findOriginalArray([6, 3, 0, 1])
