# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        val = root.val
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val != val:
                return False

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return True