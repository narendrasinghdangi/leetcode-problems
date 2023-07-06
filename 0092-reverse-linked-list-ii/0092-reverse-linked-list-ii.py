# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        li=[]
        k=1
        r=head
        while r:
            if k>=left and k<=right:
                li.append(r.val)
            r=r.next
            k=k+1
        r=head
        k=1
        while r:
            if k>=left and k<=right:
                r.val=li.pop()
            r=r.next
            k=k+1
        return head