# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev_node = None
        node = slow
        while node:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node

        left_node = head
        right_node = prev_node
        while left_node and right_node:
            if left_node.val != right_node.val:
                return False

            left_node = left_node.next
            right_node = right_node.next

        return True

# Time: O(N)
# Space: O(1)
