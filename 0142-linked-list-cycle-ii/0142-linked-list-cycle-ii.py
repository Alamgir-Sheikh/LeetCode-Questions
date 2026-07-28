# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        # print(head)
        fast = head
        slow = head
        is_cycle_detected = False

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            # print(f"Fast: {fast}")
            # print(f"Slow: {slow}")

            if fast == slow:
                is_cycle_detected = True
                break
        if is_cycle_detected:
            slow = head
            while slow or fast:
                if slow == fast:
                    return slow
                slow = slow.next
                fast = fast.next
        return None