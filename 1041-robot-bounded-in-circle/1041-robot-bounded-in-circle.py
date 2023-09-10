class Solution:
    def isRobotBounded(self, ins: str) -> bool:
        a=[0,0]
        b=[0,0]
        d=0
        for j in range(100):
            for i in ins:
                if i=="L":
                    d=d-1
                    d=d%4
                if i=="R":
                    d=d+1
                    d=d%4
                if i=="G":
                    if d==0:
                        a=[a[0],a[1]+1]
                    if d==1:
                        a=[a[0]+1,a[1]]
                    if d==2:
                        a=[a[0],a[1]-1]
                    if d==3:
                        a=[a[0]-1,a[1]]
            
            if a==b:
                return True
        return False