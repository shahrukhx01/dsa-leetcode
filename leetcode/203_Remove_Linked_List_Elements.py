# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if head is None:
            return

        dummy = head

        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
                continue

            elif head.val == val:
                dummy = head.next
                head = head.next
                continue
            head = head.next

        if head.val == val:
            dummy = None

        return dummy
