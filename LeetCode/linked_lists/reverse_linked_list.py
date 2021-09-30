# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = None
        if not head:
            return None

        while True:
            # Exit if reached the last node
            if not head.next:
                head.next = left
                break

            # Store next node's value
            next_tmp = head.next
            # Set current pointing to left node
            head.next = left
            # Update left node's value
            left = head
            # Change current to next node
            head = next_tmp

        return head
