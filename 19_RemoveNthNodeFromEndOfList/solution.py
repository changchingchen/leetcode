# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or (not head.next and n == 1):
            return None

        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next

        if n == len(nodes):
            head.next = None
            head = nodes[1]
        elif n == 1:
            nodes[-2].next = None
        else:
            nodes[-n-1].next = nodes[-n+1]
            nodes[-n].next = None

        return head

# Time: O(N)
# Space: O(N)