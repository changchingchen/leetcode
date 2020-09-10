# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head

        tail = head
        n = 1 # total node count
        while(tail.next):
            tail = tail.next
            n += 1

        k = k % n
        if k == 0:
            return head

        node = head
        i = 1
        while i < n-k:
            node = node.next
            i += 1

        tail.next = head
        head = node.next
        node.next = None

        return head
