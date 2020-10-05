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

        if root.left:
            self.flatten(root.left)

        if root.right:
            self.flatten(root.right)

        right_node = root.right
        root.right = root.left
        root.left = None

        node = root
        while node.right:
            node = node.right

        node.right = right_node
