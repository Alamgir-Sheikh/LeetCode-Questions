# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp = head
        first: ListNode = ListNode(0)
        first_temp = first
        second: ListNode = ListNode(0)
        second_temp = second

        while temp:
            if temp.val < x:
                first_temp.next = temp
                # first_temp.next = None
                first_temp = first_temp.next
            else:
                second_temp.next = temp
                # second_temp.next = None
                second_temp = second_temp.next
            temp = temp.next
        second_temp.next = None
        first_temp.next = second.next
        # print(first)
        return first.next