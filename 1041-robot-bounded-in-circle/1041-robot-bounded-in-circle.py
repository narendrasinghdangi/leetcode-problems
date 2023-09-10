class Solution:
    def isRobotBounded(self, ins: str) -> bool:
        a=[0,0]
        d=0
        for i in ins:
            if i=="L":
                d=d-1
                d=d%4
            if i=="R":
                d=d+1
                d=d%4
            if i=="G":
                if d==0:
                    a[1]=a[1]+1
                if d==1:
                    a[0]=a[0]+1
                if d==2:
                    a[1]=a[1]-1
                if d==3:
                    a[0]=a[0]-1
        return a==[0,0] or d!=0