# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d={}
        while head:  
            a=head.val
            if a in d:
                d[a]=d[a]+1
            else:
                d[a]=1
            
            head=head.next
        li=[]
        for i in d:
            if d[i]==1:
                li.append(i)
        li=li[::-1]
        lol=ListNode()
        a=lol
        for i in range(len(li)):
            lol.next=ListNode(li.pop())
            lol=lol.next
        return a.next
        