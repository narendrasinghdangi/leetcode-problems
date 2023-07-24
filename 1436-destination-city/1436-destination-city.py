class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        li=[p[0] for p in paths]
        for i in paths:
            if i[1] not in li:
                return i[1]