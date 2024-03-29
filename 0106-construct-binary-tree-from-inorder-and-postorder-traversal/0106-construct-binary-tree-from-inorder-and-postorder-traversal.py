# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:   
        if not inorder:
            return
        root=TreeNode(postorder.pop())
        root_i=inorder.index(root.val)
        
        root.left=self.buildTree(inorder[:root_i],postorder[:root_i])
        root.right=self.buildTree(inorder[root_i+1:],postorder[root_i:])
        return root

