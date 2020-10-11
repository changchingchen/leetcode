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
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child))

        return 1 + max_depth

# Time: O(N)
# Space: O(h), h: height of Tree, at most h of call stack in recursion
