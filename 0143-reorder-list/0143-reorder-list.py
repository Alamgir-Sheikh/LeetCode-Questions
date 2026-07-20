# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self, l: Optional[ListNode]) -> Optional[ListNode]:
        curr = l
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head


        # Splitting the list
        fast = slow = head
        # slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second list
        second_half = slow.next
        slow.next = None
        reversed_list = self.reverse_list(second_half)
        
        temp = ListNode(-1)
        tail = temp
        head_temp = head
        
        while head_temp and reversed_list:
            tail.next = head_temp
            tail = tail.next
            head_temp = head_temp.next
            tail.next = reversed_list
            tail = tail.next
            reversed_list = reversed_list.next
        
        if head_temp:
            tail.next = head_temp
        if reversed_list:
            tail.next = reversed_list