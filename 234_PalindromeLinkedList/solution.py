# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        size = 0
        node = head
        while node:
            size += 1
            node = node.next

        prev_node = None
        node = head
        for i in range(size//2):
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node

        left_node = prev_node
        right_node = node if size % 2 == 0 else node.next
        while left_node and right_node:
            if left_node.val != right_node.val:
                return False

            left_node = left_node.next
            right_node = right_node.next

        return True

# Time: O(N)
# Space: O(1)
