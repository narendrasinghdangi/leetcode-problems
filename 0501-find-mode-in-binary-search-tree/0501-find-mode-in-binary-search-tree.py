# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d={}
        def DFS(node):
            if node:
                if node.val in d:
                    d[node.val]=d[node.val]+1
                else:
                    d[node.val]=1
                DFS(node.left)
                DFS(node.right)
        DFS(root)
        m=0
        for i in d:
            if d[i]>m:
                m=d[i]
        lol=[]
        for i in d:
            if d[i]==m:
                lol.append(i)
        return lol