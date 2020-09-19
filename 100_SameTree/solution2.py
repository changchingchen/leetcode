# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack_p = [p]
        stack_q = [q]
        while stack_p and stack_q:
            node_p = stack_p.pop()
            node_q = stack_q.pop()
            if (node_p and not node_q) or (node_q and not node_p):
                return False

            if node_p and node_q:
                if node_p.val != node_q.val:
                    return False

                stack_p.extend([node_p.right, node_p.left])
                stack_q.extend([node_q.right, node_q.left])

        return True
