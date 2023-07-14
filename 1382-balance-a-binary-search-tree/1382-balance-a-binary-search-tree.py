# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        li=[]
        def DFS(node):
            if node:   
                DFS(node.left)
                li.append(node.val)
                DFS(node.right)
        DFS(root)
        def balanced(left,right,nums):
            if left > right:
                return None
            else:
                mid = (left + right)//2
                root = TreeNode(nums[mid])
                root.left = balanced(left,mid-1,nums)
                root.right = balanced(mid+1,right,nums)
            return root
        return balanced(0,len(li)-1,li)