# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head is not None:
            arr.append(head)
            head = head.next
        len_arr = len(arr)
        if len_arr%2==0:
            return arr[int(len_arr/2)]
        else:
            return arr[int((len_arr-1)/2)]

        
