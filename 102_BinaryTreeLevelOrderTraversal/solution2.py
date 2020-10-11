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
        q = deque([root])
        lv = 0
        while q:
            ans.append([])
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                ans[lv].append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            lv += 1

        return ans

# Time: O(N)
# Space: O(N)