# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        if head is None:
            return

        binary_num = ""
        while head:
            binary_num += str(head.val)
            head = head.next

        return int(binary_num, 2)
