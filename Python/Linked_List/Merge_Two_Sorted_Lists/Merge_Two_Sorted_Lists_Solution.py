class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def Node2Arr(currentNode):
            nodearr = []
            while currentNode:
                nodearr.append(currentNode.val)
                currentNode = currentNode.next
            return nodearr
        def Arr2Node(arr):
            temp = ListNode()
            current = temp
            for val in arr:
                current.next = ListNode(val)
                current = current.next
            return temp.next
        
        combinedarr = sorted(Node2Arr(list1) + Node2Arr(list2))
        
        merged_list = Arr2Node(combinedarr)
        
        return merged_list
