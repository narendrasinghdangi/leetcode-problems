class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        l = len(arr)
        d = Counter(arr)
        c = 0
        m = 0
        li = list(d.values())
        li.sort(reverse=True)
        for i in li:
            c = c+1
            m = m+i
            if m >= l//2:
                return c