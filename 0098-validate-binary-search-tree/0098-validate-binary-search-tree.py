# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        li=[]
        def DFS(node):
            if node:
                DFS(node.left)
                li.append(node.val)
                DFS(node.right)
        DFS(root)
        return li==list(sorted(set(li)))
                        