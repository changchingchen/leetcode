# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        new_list = [None] * k

        if not root:
            return new_list

        size = 0
        node = root
        while node:
            size += 1
            node = node.next

        quotient = size // k
        remainder = size % k
        node = root
        for i in range(k):
            sublist_size = quotient
            if remainder > 0:
                sublist_size += 1
                remainder -= 1

            size -= sublist_size
            new_list[i] = node
            while sublist_size > 1:
                node = node.next
                sublist_size -= 1

            next_node = node.next
            node.next = None
            node = next_node
            if size <= 0:
                break

        return new_list
