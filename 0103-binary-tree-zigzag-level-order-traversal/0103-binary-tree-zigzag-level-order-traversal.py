# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        q=[root]
        ans=[]
        while q:
            li=[]
            qlen=len(q)
            for i in range(qlen):
                node=q.pop(0)
                li.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(li)
        for i in range(len(ans)):
            if i%2!=0:
                ans[i]=ans[i][::-1]
        return ans