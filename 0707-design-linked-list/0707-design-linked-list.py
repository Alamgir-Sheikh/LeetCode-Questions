class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0  # Tracking size makes index validation trivial
        

    def get(self, index: int) -> int:
        # Validate index
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val


    def addAtHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node
        self.size += 1


    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        # If index is greater than the length, the node will not be inserted.
        if index > self.size:
            return
        # If index is negative or 0, the node will be inserted at the head.
        if index <= 0:
            self.addAtHead(val)
            return

        curr = self.head
        # Traverse to the node right BEFORE the insertion point (index - 1)
        for _ in range(index - 1):
            curr = curr.next
            
        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        # Validate index
        if index < 0 or index >= self.size:
            return
        
        # Case 1: Delete the head node
        if index == 0:
            self.head = self.head.next
        else:
            # Case 2: Delete a node in the middle or end
            curr = self.head
            # Traverse to the node right BEFORE the one we want to delete
            for _ in range(index - 1):
                curr = curr.next
            
            # Skip the target node
            curr.next = curr.next.next
            
        self.size -= 1
    
    # def print_nodes(self):
    #     temp = self.head
    #     while temp:
    #         print(temp.val, end="")
    #         if temp.next is not None:
    #             print(" -> ", end="")
    #         temp = temp.next
    #     print()

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)