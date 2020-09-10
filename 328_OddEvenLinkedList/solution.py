# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        even_head = head.next
        odd_tail = node = head
        cnt = 1
        while node.next:
            next_node = node.next
            node.next = next_node.next

            if cnt % 2 != 0:
                odd_tail = node

            node = next_node
            cnt += 1

        if cnt % 2 != 0:
            odd_tail = node

        odd_tail.next = even_head

        return head
