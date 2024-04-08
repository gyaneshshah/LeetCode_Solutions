# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        ans = head
        temp = head
        arr = []
        while temp:
            arr.append(temp)
            temp = temp.next
        prev = arr[len(arr)//2-1]
        middle = prev.next
        prev.next = middle.next
        middle.next = None
        return ans
