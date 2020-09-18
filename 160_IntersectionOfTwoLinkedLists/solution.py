# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        size_a = size_b = 0
        node_a, node_b = headA, headB
        while node_a or node_b:
            if node_a:
                size_a += 1
                node_a = node_a.next

            if node_b:
                size_b += 1
                node_b = node_b.next

        node_a, node_b = headA, headB
        if size_a > size_b:
            for _ in range(size_a - size_b):
                node_a = node_a.next
        elif size_a < size_b:
            for _ in range(size_b - size_a):
                node_b = node_b.next

        while node_a and node_b:
            if node_a == node_b:
                return node_a

            node_a = node_a.next
            node_b = node_b.next

        return None

# Time: O(max(sizeA, sizeB))
# Space: O(1)