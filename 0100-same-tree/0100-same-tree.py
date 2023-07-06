# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def DFS(node1,node2):
            if node1:
                if not node2:
                    f[0]=0
                    return
            if node2:
                if not node1:
                    f[0]=0
                    return
            if node1 and node2:
                if node1.val!=node2.val:
                    f[0]=0
                    return
                DFS(node1.left,node2.left)
                DFS(node1.right,node2.right)
        f=[1]
        DFS(p,q)
        return f==[1]