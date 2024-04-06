# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head is None:
            return None
        temp = head
        string_num = ""
        while temp:
            string_num += str(temp.val)
            temp = temp.next
        return int(string_num, 2)
