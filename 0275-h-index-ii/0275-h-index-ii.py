class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations=citations[::-1]
        for h in range(len(citations)):
            if h>=citations[h]:
                return h
        return len(citations)