# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return

        node = root
        stack = []
        while node:
            if node.right:
                stack.append(node.right)

            node.left, node.right = None, node.left
            if not node.right and stack:
                node.right = stack.pop()

            node = node.right
