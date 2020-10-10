# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        dq = deque([(root, 1)])
        while dq:
            node, d = dq.popleft()
            if not node.left and not node.right:
                return d

            if node.left:
                dq.append((node.left, d+1))

            if node.right:
                dq.append((node.right, d+1))
