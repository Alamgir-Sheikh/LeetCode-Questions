# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next and n == 1:
            return head.next
        temp = head
        size: int = 0

        # Getting the total number of nodes
        while temp:
            size += 1
            temp = temp.next
        
        # If size equals n means we have to remove the first node
        if size == n:
            print(f"Size is equal to N")
            return head.next
        
        del_temp = head
        itr = 0
        skip_nodes = size - n - 1
        print(f"Skip nodes: {skip_nodes}")
        while itr < skip_nodes:
            del_temp = del_temp.next
            itr += 1
        print(f"Current node: {del_temp}")
        del_temp.next = del_temp.next.next
        print(del_temp)
        print(head)
        return head