# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return None

        size = 0
        fast_node = head
        slow_node = ListNode(0, head) # dummy node
        while fast_node:
            size += 1
            fast_node = fast_node.next
            if size > n:
                slow_node = slow_node.next

        if n == size:
            head = slow_node.next.next
            slow_node.next.next = None
        else:
            removed_node = slow_node.next
            slow_node.next = removed_node.next
            removed_node.next = None        

        return head

# Time: O(N), one pass
# Space: O(1)