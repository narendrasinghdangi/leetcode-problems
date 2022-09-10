class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        li = []
        p = [i for i in range(1, m+1)]
        print(p)
        print(queries)
        for i in range(len(queries)):
            po = p.index(queries[i])
            li.append(po)
            lol = p[po]
            for j in range(po, 0, -1):
                p[j] = p[j-1]
            p[0] = lol
            print(p)
        print(li)


s = Solution()
s.processQueries([2, 2, 4, 6, 8, 4, 4], 8)
