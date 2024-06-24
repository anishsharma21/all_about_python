class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def prepend(self, value): ##
        new_head = Node(value, self.head)
        self.head = new_head
        return new_head

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = Node(value)
        return cur_node.next
    
    def insert_after_value(self, value, target):
        if not self.head:
            print("\nlist is empty...\n")
        cur_node = self.head
        while cur_node:
            if cur_node.value == target:
                cur_node.next = Node(value, cur_node.next)
                return cur_node.next
            cur_node = cur_node.next
        print("\ntarget value not found :(\n")
