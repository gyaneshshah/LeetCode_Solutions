# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def LengthOfNode(node):
            count = 0
            while (node):
                count +=1
                node = node.next
            return count

        # Calculate the index
        index = LengthOfNode(head) - n

        if index == 0:
            return head.next
        
        current_node = head
        count = 0
        
        # Traverse the list to find the node before the one to be removed
        while current_node and count < index - 1:
            current_node = current_node.next
            count += 1
        
        # Update the links to remove the node
        current_node.next = current_node.next.next
        
        return head
