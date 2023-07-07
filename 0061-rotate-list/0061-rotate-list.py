# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        li=[]
        r=head
        while r:
            li.append(r.val)
            r=r.next
        l=k%len(li)
        li=li[len(li)-l:]+li[:len(li)-l]
        lol=ListNode()
        a=lol
        for i in range(len(li)):
            lol.next=ListNode(li[i])
            lol=lol.next
        return a.next
        