# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        li=[]
        def BST(node):
            if node:
                li.append(node.val)
                BST(node.left)
                BST(node.right)
            
        BST(root)
        m=float("inf")
        for i in range(len(li)):
            for j in range(i,len(li)):
                if abs(li[i]-li[j])<m and i!=j:
                    m=abs(li[i]-li[j])
        return m
                
        
        
                