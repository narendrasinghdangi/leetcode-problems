class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d={}
        for i in range(len(heights)):
            d[i]=heights[i]
        print(d)
        d=dict(sorted(d.items(), key=lambda x:x[1]))
        li=[i for i in d]
        li=[names[i] for i in li]
        return li[::-1]
            
        