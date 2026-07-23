# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_head = ListNode()
        temp = sum_head
        carry = 0
        while l1 and l2:
            res = l1.val + l2.val + carry
            if res >= 10:
                carry = 1
                res = res % 10
            else:
                carry = 0
            # print(f"res: {res}, carry: {carry}")

            new_node = ListNode(res)
            temp.next = new_node
            temp = temp.next
            # print(sum_head)
            l1 = l1.next
            l2 = l2.next
        while l1:
            res = l1.val + carry
            if res >= 10:
                carry = 1
                res = res % 10
            else:
                carry = 0
            new_node = ListNode(res)
            temp.next = new_node
            temp = temp.next
            l1 = l1.next
        
        while l2:
            res = l2.val + carry
            if res >= 10:
                carry = 1
                res = res % 10
            else:
                carry = 0
            new_node = ListNode(res)
            temp.next = new_node
            temp = temp.next
            l2 = l2.next
        
        if carry:
            new_node = ListNode(carry)
            temp.next = new_node

        return sum_head.next