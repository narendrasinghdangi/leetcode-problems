class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        li=[]
        d=Counter(nums)
        d=dict(sorted(d.items(),key=lambda  item:item[1],reverse=True))
        c=0
        for i in d:
            li.append(i)
            c=c+1
            if k==c:
                break
        return li