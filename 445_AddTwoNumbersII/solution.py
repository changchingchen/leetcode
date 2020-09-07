# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x = l1.val
        node = l1.next
        while node:
            x = x * 10 + node.val
            node = node.next

        if x == 0:
            return l2

        y = l2.val
        node = l2.next
        while node:
            y = y * 10 + node.val
            node = node.next

        if y == 0:
            return l1

        z = x + y
        prev_node = None
        while z > 0:
            node = ListNode(z%10, prev_node)
            prev_node = node
            z //= 10

        return node
