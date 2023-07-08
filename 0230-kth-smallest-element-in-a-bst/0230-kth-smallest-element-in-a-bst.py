# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        li=[]
        def DFS(node):
            if node:
                li.append(node.val)
                DFS(node.left)
                DFS(node.right)
        DFS(root)
        li.sort()
        return li[k-1]