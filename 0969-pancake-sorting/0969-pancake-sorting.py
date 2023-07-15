class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        i=0
        j=len(arr)-1
        li=[]
        while len(arr)>1:
            i=arr.index(max(arr))
            if i!=0:
                li.append(i+1)
                k=arr[:i+1]
                k=k[::-1]
                arr=k+arr[i+1:]
            li.append(j+1)
            arr=arr[::-1]
            arr=arr[:j]
            j=j-1
        return li
                