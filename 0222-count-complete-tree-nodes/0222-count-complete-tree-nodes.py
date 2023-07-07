# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def DFS(node):
            if node:
                li.append(node.val)
                DFS(node.left)
                DFS(node.right)
                
        li=[]
        DFS(root)
        return len(li)
        