class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def set_head(self, value):
        new_head_node = Node(value, self.head)
        self.head = new_head_node
    
    def is_empty(self):
        if not self.head:
            return True
        return False
    
    def append(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
        return new_node
            
    def traverse(self):
        cur_node = self.head
        while cur_node:
            print(str(cur_node.value), end='')
            if cur_node.next:
                print(" --> ", end='')
            cur_node = cur_node.next
        print()
    
    def insert_after_value(self, target, value):
        if self.is_empty():
            print("list is empty...\n")
            return
        cur_node = self.head
        while cur_node:
            if cur_node.value == target:
                new_node = Node(value)
                new_node.next = cur_node.next
                cur_node.next = new_node
                return new_node
            cur_node = cur_node.next
        print(f"target value, '{target}', not found...\n")
    
    def delete_by_value(self, target):
        if self.is_empty():
            print("list is empty...\n")
            return
        if self.head.value == target:
            self.head = self.head.next
            return
        prev_node = self.head
        while prev_node.next:
            if prev_node.next.value == target:
                prev_node.next = prev_node.next.next
                return
            prev_node = prev_node.next
        print(f"target value, '{target}', not found...\n")

node1 = Node(5)
sll = SinglyLinkedList(node1)
sll.traverse()
sll.set_head(4)
sll.traverse()
appended_node = sll.append(2)
sll.traverse()
sll.set_head(1)
sll.traverse()
sll.insert_after_value(4, 9)
sll.traverse()
sll.insert_after_value(2, 13)
sll.traverse()
sll.delete_by_value(1)
sll.traverse()