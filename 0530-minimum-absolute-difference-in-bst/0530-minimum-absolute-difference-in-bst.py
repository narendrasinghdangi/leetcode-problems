# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        li=[]
        def DFS(node):
            if node:
                li.append(node.val)
                DFS(node.left)
                DFS(node.right)
        DFS(root)
        m=10**5
        for i in range(len(li)):
            for j in range(i+1,len(li)):
                if abs(li[i]-li[j])<m:
                    m=abs(li[i]-li[j])
        return m
        
        
                