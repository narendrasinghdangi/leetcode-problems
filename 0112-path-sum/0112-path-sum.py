# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def DFS(node,m):
            if node:
                m=m+node.val
                DFS(node.left,m)
                DFS(node.right,m)
                if not node.left and not node.right:
                    if m==targetSum:
                        ma[0]=1
        ma=[0]        
        DFS(root,0)
        return ma[0]==1