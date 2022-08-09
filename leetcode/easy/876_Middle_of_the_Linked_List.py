# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        size = 0
        cursor = head

        while cursor:
            size += 1
            cursor = cursor.next

        middle_index = size // 2

        idx = 0

        cursor = head
        while cursor:
            if idx == middle_index:
                return cursor

            idx += 1
            cursor = cursor.next
