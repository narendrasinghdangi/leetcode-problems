```
class Solution:
def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
if not inorder: return
​
root = TreeNode(postorder[-1])
root_value_i = inorder.index(root.val)
​
root.left = self.buildTree(inorder[:root_value_i], postorder[:root_value_i])
root.right = self.buildTree(inorder[root_value_i+1:], postorder[root_value_i:-1])
return root
```