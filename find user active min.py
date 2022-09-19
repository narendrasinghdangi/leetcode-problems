from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        d = defaultdict(list)
        l = [0]*k
        for i in logs:
            if i[1] not in d[i[0]]:
                d[i[0]].append(i[1])
        for i in d.values():
            if l[len(i)-1] > 0:
                l[len(i)-1] = l[len(i)-1]+1
            else:
                l[len(i)-1] = 1
        print(l)


s = Solution()
s.findingUsersActiveMinutes([[1, 1], [2, 2], [2, 3]], 4)
