from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[]
        d=defaultdict(list)
        q.append([root,0,0])
        while q:
            node,r,c=q.pop(0)
            d[c].append([r,node.val])
            if node.left:
                q.append([node.left,r+1,c-1])
            if node.right:
                q.append([node.right,r+1,c+1])
        ans=[]
        for i in sorted(d):
            lol=d[i]
            lol.sort()
            t=[]
            for j in lol:
                t.append(j[1])
            ans.append(t)
        return ans