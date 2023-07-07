# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def DFS(node,m):
            if node:
                m=m*10+node.val
                DFS(node.left,m)
                DFS(node.right,m)
                if not node.left and not node.right:
                    li.append(m)
        li=[]
        DFS(root,0)
        return sum(li)