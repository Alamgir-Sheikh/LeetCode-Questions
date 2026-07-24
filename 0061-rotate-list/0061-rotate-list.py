# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, first: Optional[ListNode], second: Optional[ListNode]) -> Optional[ListNode]:
        s_temp = second

        while s_temp.next:
            s_temp = s_temp.next
        s_temp.next = first
        # print(f"S_Temp; {second}")
        return second

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        size: int = 0
        size_temp = head

        while size_temp:
            size += 1
            size_temp = size_temp.next
        k_effective = k % size

        if k_effective == 0:
            return head
        skip_nodes = size - (k_effective)
        # print(f"Size: {size}")
        # print(f"Nodes to skip: {skip_nodes}")


        first = temp = head
        second = None
        itr = 1
        while itr < skip_nodes:
            temp = temp.next
            itr += 1
        
        
        second = temp.next
        temp.next = None
        # print(f"First: {first}")
        # print(f"Temp: {temp}")
        # print(f"Second: {second}")

        return self.merge(first, second)

