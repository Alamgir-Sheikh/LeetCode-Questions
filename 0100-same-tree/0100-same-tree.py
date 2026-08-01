# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. Base case: both nodes are empty -> structurally identical here
        if not p and not q:
            return True
        # 2. Base case: one is empty and the other isn't -> structural mismatch
        if not p or not q:
            return False
        
        # 3. Base case: values don't match
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)