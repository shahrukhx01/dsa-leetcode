# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Keep marking the seen nodes, hence if you encounter the seen node again you'd know ;)
        """

        while head:
            if not head.val:
                return True

            head.val = None
            head = head.next

        return False
