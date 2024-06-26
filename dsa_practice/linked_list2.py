class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def prepend(self, value):
        self.head = Node(value, self.head)
        return self.head
    
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
            print("list is empty")
            return None
        cur_node = self.head
        while cur_node:
            if cur_node.value == target:
                new_node = Node(value, cur_node.next)
                cur_node.next = new_node
                return new_node
            cur_node = cur_node.next
        print("target value not found")
        return None
    
    def delete_by_value(self, target):
        if not self.head:
            print("list is empty")
            return None
        if self.head.value == target:
            deleted_node, self.head = self.head, self.head.next
            return deleted_node
        cur_node = self.head
        while cur_node.next:
            if cur_node.next.value == target:
                cur_node.next, deleted_node = cur_node.next.next, cur_node.next
                return deleted_node
            cur_node = cur_node.next
        print("target value not found")
        return None
    
    def delete_by_position(self, position):
        if position < 1:
            print("position must be >= 1")
            return None
        if not self.head:
            print("list is empty")
            return None
        if position == 1:
            self.head = self.head.next
            return True
        track = 2
        cur_node = self.head
        while cur_node:
            if track == position:
                cur_node.next, deleted_node = cur_node.next.next, cur_node.next
                deleted_node.next = None
                return True
            cur_node = cur_node.next
            track += 1
        print("position out of bounds")
        return False

    def delete_head(self):
        if not self.head:
            print("list is empty")
            return None
        self.head, deleted_head = self.head.next, self.head
        return deleted_head
    
    def delete_last_node(self):
        if not self.head or not self.head.next:
            deleted_node, self.head = self.head, None
        else:
            cur_node = self.head
            while cur_node.next.next:
                cur_node = cur_node.next
            deleted_node, cur_node.next = cur_node.next, cur_node.next.next
        return deleted_node

    def search(self, target) -> Node:
        if not self.head:
            print("list is empty")
            return None
        cur_node = self.head
        while cur_node:
            if cur_node.value == target:
                return cur_node
            cur_node = cur_node.next
        print("target value not found")
        return None
    
    def traverse(self):
        if not self.head:
            print("None (empty)")
            return
        print(self.head.value, end='')
        cur_node = self.head.next
        while cur_node:
            print(" -->", str(cur_node.value), end='')
            cur_node = cur_node.next
        print(" --> None")
        
    def length(self):
        length = 0
        cur_node = self.head
        while cur_node:
            length += 1
            cur_node = cur_node.next
        return length

    def reverse(self, node=None):
        if not self.head:
            print("list is empty")
            return None
        if not node:
            node = self.head
        if not node.next:
            self.head = node
            return node
        next_node = self.reverse(node.next)
        next_node.next = node
        node.next = None
        return node
    
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
        if not self.head or not self.head.next:
            return self.head
        slow = self.head
        fast = self.head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def remove_duplicates(self):
        if not self.head or not self.head.next:
            return
        counts = {self.head.value}
        cur_node = self.head
        while cur_node.next:
            if cur_node.next.value in counts:
                deleted_node, cur_node.next = cur_node.next, cur_node.next.next
                deleted_node = None
            else:
                counts.add(cur_node.next.value)
                cur_node = cur_node.next
    
    def delete_nth_from_end(self, n):
        if n < 1:
            print("nth position must be >= 1")
            return
        if not self.head:
            print("list is empty")
            return None
        length = 0
        cur_node = self.head
        while cur_node:
            length += 1
            cur_node = cur_node.next
        if n > length:
            print("nth position too large")
            return None
        pos = length - n + 1
        if pos == 1:
            deleted_head, self.head = self.head, self.head.next
            return
        track = 2
        cur_node = self.head
        while track != pos:
            track += 1
            cur_node = cur_node.next
        deleted_node, cur_node.next = cur_node.next, cur_node.next.next
        return deleted_node
            

ll = SinglyLinkedList()
values = [1, 2, 3, 4, 5]
for value in values:
    ll.append(value)
ll.traverse()
ll.delete_nth_from_end_with_methods(2)
ll.traverse()