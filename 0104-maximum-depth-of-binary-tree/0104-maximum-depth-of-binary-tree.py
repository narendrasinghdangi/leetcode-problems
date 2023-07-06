# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def DFS(node,m):
            if node:
                m=m+1
                DFS(node.left,m)
                DFS(node.right,m)
                if not node.left and not node.right:
                    if m>max[0]:
                        max[0]=m
                m=m-1
        max=[0]
        DFS(root,0)
        return max[0]
                
                