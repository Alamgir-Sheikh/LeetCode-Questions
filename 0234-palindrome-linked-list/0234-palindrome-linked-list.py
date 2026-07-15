# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_list(self, slow: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = slow
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head.next is None:
            return True
        
        fast = head.next
        slow = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next

        temp = head
        rev_list = self.reverse_list(slow)
        
        while temp and rev_list:
            if temp.val != rev_list.val:
                return False
            temp = temp.next
            rev_list = rev_list.next
        return True