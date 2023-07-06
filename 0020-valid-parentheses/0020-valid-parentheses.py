class Solution:
    def isValid(self, s: str) -> bool:
        li=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                li.append(i)
            else:
                if len(li)>0 and i==")" and li[-1]=="(":
                    li.pop()
                elif len(li)>0 and i=="}" and li[-1]=="{":
                    li.pop()
                elif len(li)>0 and i=="]" and li[-1]=="[":
                    li.pop()
                else:
                    return False
        if len(li)==0:
            return True
        else:
            return False
                    
            