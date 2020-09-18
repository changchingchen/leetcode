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

        node_map = {}
        node = head
        while node:
            if node not in node_map:
                node_map[node] = Node(node.val)

            next_node = node.next
            if not next_node:
                node_map[node].next = next_node
            elif next_node in node_map:
                node_map[node].next = node_map[next_node]
            else:
                node_map[next_node] = Node(next_node.val)
                node_map[node].next = node_map[next_node]

            random_node = node.random
            if not random_node:
                node_map[node].random = random_node
            elif random_node in node_map:
                node_map[node].random = node_map[random_node]
            else:
                node_map[random_node] = Node(random_node.val)
                node_map[node].random = node_map[random_node]

            node = node.next

        return node_map[head]

# Time: O(N)
# Space: O(N)