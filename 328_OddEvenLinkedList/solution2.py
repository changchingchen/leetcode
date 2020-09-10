# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        even_head = even_tail = head.next
        odd_tail = head
        while(odd_tail.next and even_tail.next):
            odd_tail.next = odd_tail.next.next
            odd_tail = odd_tail.next
            even_tail.next = even_tail.next.next
            even_tail = even_tail.next

        odd_tail.next = even_head

        return head
