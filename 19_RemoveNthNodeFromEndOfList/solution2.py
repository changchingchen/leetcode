# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not head.next:
            return None

        size = 0
        node = head
        while node:
            size += 1
            node = node.next

        node = head
        if n == size:
            head = node.next
            node.next = None
        else:
            k = size - n - 1
            while k > 0:
                node = node.next
                k -= 1

            removed_node = node.next
            node.next = removed_node.next
            removed_node.next = None        

        return head

# Time: O(N), two pass
# Space: O(1)