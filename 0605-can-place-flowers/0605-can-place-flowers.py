class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1 and flowerbed[0]==0:
            return True
        if len(flowerbed)==1 and flowerbed[0]==1 and n==1:
            return False
        
            
        c=0
        if flowerbed[0]==0 and flowerbed[1]==0:
            flowerbed[0]=1
            c=c+1
        
        for i in range(2,len(flowerbed)-1):
            if flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i-1]==0:
                c=c+1
                flowerbed[i]=1
        if flowerbed[-1]==0 and flowerbed[-2]==0:
            c=c+1
        return c>=n
                    
                