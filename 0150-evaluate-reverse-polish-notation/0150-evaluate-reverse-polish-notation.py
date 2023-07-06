class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        li=[]
        for i in range(len(tokens)):
            if tokens[i]=="+":
                a=li.pop()
                b=li.pop()
                li.append(a+b)
            elif tokens[i]=="*":
                a=li.pop()
                b=li.pop()
                li.append(a*b)
            elif tokens[i]=="-":
                a=li.pop()
                b=li.pop()
                li.append(b-a)
            elif tokens[i]=="/":
                a=li.pop()
                b=li.pop()
                li.append(int(float(b)/a))
            else:
                li.append(int(tokens[i]))
        return li[0]