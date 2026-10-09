# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if child exists, explore root.left, root.right, + 1 for each traversal
        # take the max of each branch
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))