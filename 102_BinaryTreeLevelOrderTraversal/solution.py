# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = deque([(root, 0)])
        nodes = []
        prev_lv = 0
        while q:
            node, lv = q.popleft()
            if lv != prev_lv:
                ans.append(nodes)
                nodes = []

            nodes.append(node.val)
            prev_lv = lv

            if node.left:
                q.append((node.left, lv+1))
            
            if node.right:
                q.append((node.right, lv+1))

        ans.append(nodes)

        return ans

# Time: O(N)
# Space: O(N)