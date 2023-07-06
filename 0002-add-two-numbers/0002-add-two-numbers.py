# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        while l1!=None:
            s1=s1+str(l1.val)
            l1=l1.next
        s2=""
        while l2!=None:
            s2=s2+str(l2.val)
            l2=l2.next
        s3=str(int(s1[::-1])+int(s2[::-1]))[::-1]
        l=ListNode(int(s3[0]))
        itr=l
        i=1
        while len(s3)>i:
            itr.next=ListNode(int(s3[i]))
            itr=itr.next
            i=i+1
        return l