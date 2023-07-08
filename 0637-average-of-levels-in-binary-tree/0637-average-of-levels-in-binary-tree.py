# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=[root]
        ans=[]
        while q:
            row=0
            qlen=len(q)
            for i in range(qlen):
                node=q.pop(0)
                row=row+node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(row/qlen)
        return ans
            