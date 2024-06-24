import pytest
from linked_list2 import Node, SinglyLinkedList

def test_prepend():
    sll = SinglyLinkedList(None)
    sll.prepend(1)
    assert sll.head.value == 1
    sll.prepend(2)
    assert sll.head.value == 2
    assert sll.head.next.value == 1

def test_append():
    sll = SinglyLinkedList(None)
    sll.append(1)
    assert sll.head.value == 1
    sll.append(2)
    assert sll.head.next.value == 2
    sll.append(3)
    assert sll.head.next.next.value == 3

def test_insert_after_value():
    sll = SinglyLinkedList(Node(1))
    sll.append(2)
    sll.append(4)
    sll.insert_after_value(3, 2)
    assert sll.head.next.next.value == 3
    assert sll.head.next.next.next.value == 4
    sll.insert_after_value(5, 4)
    assert sll.head.next.next.next.next.value == 5

if __name__ == "__main__":
    pytest.main()
