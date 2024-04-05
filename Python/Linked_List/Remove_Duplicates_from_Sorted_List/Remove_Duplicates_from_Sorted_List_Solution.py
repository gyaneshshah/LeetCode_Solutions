# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        ans = head
        if head is None:
            return None
        while head.next:
            if head.val == head.next.val:
                temp = head.next
                head.next = temp.next
                temp.next = None
            else:
                head = head.next
        return ans
