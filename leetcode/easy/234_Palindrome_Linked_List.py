# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        dummy = ListNode()
        dummy.next = head

        stack = []

        while head:
            stack.append(head.val)
            head = head.next

        head = dummy.next

        while head:
            if head.val != stack.pop():
                return False

            head = head.next

        return True
