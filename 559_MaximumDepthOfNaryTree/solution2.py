"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        max_depth = 0
        q = deque([root])
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                q.extend(node.children)

            max_depth += 1

        return max_depth
