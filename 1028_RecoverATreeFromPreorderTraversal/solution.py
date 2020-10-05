# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:

        def create_tree(stack, start_idx, end_idx, depth):
            node = TreeNode(int(S[start_idx:end_idx]))
            while stack:
                if stack[-1][-1] == depth - 1:
                    if not stack[-1][0].left:
                        stack[-1][0].left = node
                    else:
                        stack[-1][0].right = node
                    break
                else:
                    stack.pop()
            stack.append((node, depth))

        stack = []
        start_idx = 0
        depth = 0
        is_digit = False
        for i in range(len(S)):
            if not is_digit:
                if S[i] != '-':
                    start_idx = i
                    is_digit = True
                else:
                    depth += 1
            elif S[i] == '-':
                create_tree(stack, start_idx, i, depth)
                depth = 1
                is_digit = False

        create_tree(stack, start_idx, len(S), depth)

        return stack[0][0]
