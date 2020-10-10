# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node, d):
            if not node:
                return d - 1

            left_depth = dfs(node.left, d+1)
            right_depth = dfs(node.right, d+1)

            return max(left_depth, right_depth)

        return dfs(root, 1)
