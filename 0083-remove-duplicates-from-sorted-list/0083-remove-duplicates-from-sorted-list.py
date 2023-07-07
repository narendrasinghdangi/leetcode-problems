# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        li=[head.val]
        lol=head
        b=lol.next
        while b:
            a=b.val
            if a in li:
                lol.next=lol.next.next
                b=b.next
            else:
                li.append(a)
                lol=lol.next
                b=b.next
        return head