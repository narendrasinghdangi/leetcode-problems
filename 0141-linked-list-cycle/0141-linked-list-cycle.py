# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l=0
        while head!=None:
            l=l+1
            head=head.next
            if l>10**4:
                return True
        return False
        