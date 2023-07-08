# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        ans=[]
        q=[root]
        while q:        
            ans.append(q[-1].val)
            lv=[]
            for node in q:
                if node.left:
                    lv.append(node.left)
                if node.right:
                    lv.append(node.right)
            q=lv
        return ans