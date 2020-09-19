"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        node = head
        while node:
            next_node = node.next
            node.next = Node(node.val, next_node)
            node = next_node

        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            
            node = node.next.next

        node = head
        copied_head = head.next
        while node:
            next_node = node.next.next
            copied_node = node.next
            if next_node:
                copied_node.next = next_node.next

            node.next = next_node
            node = next_node

        return copied_head

# Time: O(N)
# Space: O(1)