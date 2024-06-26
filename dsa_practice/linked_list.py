class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def is_empty(self):
        if not self.head:
            print("\nlist is empty...\n")
            return True
        return False

    def prepend(self, value): ##
        new_head = Node(value, self.head)
        self.head = new_head
        return new_head

    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return self.head
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = Node(value)
        return cur_node.next
    
    def insert_after_value(self, target, value):
        if not self.head:
            print("\nlist is empty...\n")
            return None
        cur_node = self.head
        while cur_node:
            if cur_node.value == target:
                cur_node.next = Node(value, cur_node.next)
                return cur_node.next
            cur_node = cur_node.next
        print("\ntarget value not found :(\n")
        return None

    def delete_by_value(self, target):
        if not self.head:
            print("\nlist is empty...\n")
            return None
        if self.head.value == target:
            head = self.head
            self.head = self.head.next
            return head
        node = self.head
        while node.next:
            if node.next.value == target:
                deleted_node = node.next
                node.next = node.next.next
                return deleted_node
            node = node.next
        print("\ntarget value not found...\n")
        return None
            
    def traverse(self):
        if self.is_empty():
            return
        cur_node = self.head
        while cur_node:
            print(str(cur_node.value), end='')
            if cur_node.next:
                print(" --> ", end='')
            cur_node = cur_node.next
        print()
    
    def delete_by_position(self, position):
        """Position is 1-indexed. Deletes a node at the given position."""
        if position < 1:
            print("Invalid position. Position should be >= 1.")
            return
        if self.is_empty():
            return
        if position == 1:
            self.head = self.head.next
            return
        cur_node = self.head
        track = 2
        while cur_node.next:
            if track == position:
                cur_node.next = cur_node.next.next
                return
            cur_node = cur_node.next
            track += 1
        print(f"\ntarget position, '{position}', is out of bounds...\n")
    
    def delete_head(self):
        if self.is_empty():
            return
        self.head = self.head.next
    
    def delete_last_node(self):
        if not self.head or not self.head.next:
            self.head, deleted_node = None, self.head
        else:
            cur_node = self.head
            while cur_node.next.next:
                cur_node = cur_node.next
            deleted_node = cur_node.next
        return deleted_node
    
    def search(self, target):
        if self.is_empty():
            return
        cur_node = self.head
        while cur_node:
            if cur_node.value == target:
                return cur_node
            cur_node = cur_node.next
        print("\ntarget node not found...\n")
        return None

    def length(self):
        if self.is_empty():
            return 0
        length = 0
        cur_node = self.head
        while cur_node:
            length += 1
            cur_node = cur_node.next
        return length

    def reverse(self, node=None):
        if self.is_empty():
            return
        if node == None:
            node = self.head
        if node.next == None:
            self.head = node
            return node
        next_node = self.reverse(node.next)
        next_node.next = node
        node.next = None
        return node
    
    def another_reverse(self, node=None):
        if node is None:
            if self.is_empty():
                return
            node = self.head
        if node.next is None:
            self.head = None
            return node
        next_node = self.reverse(node.next)
        node.next.next = node
        node.next = None
        return next_node
    
    def detect_loop(self):
        if not self.head:
            print("list is empty")
            return False
        slow = self.head
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
    
    def find_middle(self):
        if self.is_empty():
            return
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value
    
# Create a linked list with values 1 -> 2 -> 3
linked_list = SinglyLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# Print the original list
print("Original list:")
linked_list.traverse()

# Reverse the list
linked_list.another_reverse()

# Print the reversed list
print("Reversed list:")
linked_list.traverse()    

# node1 = Node(5)
# sll = SinglyLinkedList(node1)
# sll.traverse()
# sll.set_head(4)
# sll.traverse()
# appended_node = sll.append(2)
# sll.traverse()
# sll.set_head(1)
# sll.traverse()
# sll.insert_after_value(4, 9)
# sll.traverse()
# sll.insert_after_value(2, 13)
# sll.traverse()
# sll.delete_by_value(1)
# sll.traverse()
# print("deleting the second value")
# sll.delete_by_position(2)
# sll.traverse()
# print("deleting the last value")
# sll.delete_by_position(4)
# sll.traverse()
# sll.set_head(5)
# sll.set_head(1)
# sll.traverse()
# sll.delete_head()
# sll.traverse()
# sll.delete_last_node()
# sll.traverse()
# sll.set_head(2)
# sll.set_head(9)
# sll.set_head(5)
# sll.set_head(1)
# print("list before reverse:")
# sll.traverse()
# print()
# sll.reverse()
# print("list after reverse")
# sll.traverse()
# print(sll.head.value)