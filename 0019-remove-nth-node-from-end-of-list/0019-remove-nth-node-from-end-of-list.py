# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        a=0
        rhead=head
        while rhead:
            a=a+1
            rhead=rhead.next
        b=1
        rhead=head
        if (a-n)==0:
            return head.next
        while b!=(a-n):
            rhead=rhead.next
            b=b+1
        rhead.next=rhead.next.next
        return head
            