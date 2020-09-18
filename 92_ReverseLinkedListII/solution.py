# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        node = dummy_node = ListNode(0, head) # dummy node
        for i in range(1, n+2):
            next_node = node.next
            if i == m:
                before_reverse_node = node
                node_m = next_node
            elif i > m:
                node.next = prev_node
            
            prev_node, node = node, next_node

        node_m.next = node
        before_reverse_node.next = prev_node

        return dummy_node.next

# Time: O(N)
# Space: O(1)