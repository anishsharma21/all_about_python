import pytest
from linked_list2 import Node, SinglyLinkedList

"""prepend()"""
def test_prepend_on_empty_list():
    ll = SinglyLinkedList()
    ll.prepend(1)
    assert ll.head.value == 1, "Head should be 1"
    assert ll.head.next is None, "Next of head should be None"

def test_prepend_on_non_empty_list():
    ll = SinglyLinkedList()
    ll.prepend(2)
    ll.prepend(1)
    assert ll.head.value == 1, "Head should be 1"
    assert ll.head.next.value == 2, "Next of head should be 2"

def test_prepend_multiple_values():
    ll = SinglyLinkedList()
    values = [1, 2, 3]
    for value in values:
        ll.prepend(value)
    current = ll.head
    for value in reversed(values):
        assert current.value == value, f"Expected value {value}, got {current.value}"
        current = current.next

def test_prepend_with_various_data_types():
    ll = SinglyLinkedList()
    ll.prepend("string")
    ll.prepend(10.5)
    ll.prepend(1)
    assert ll.head.value == 1, "Head should be 1"
    assert ll.head.next.value == 10.5, "Next of head should be 10.5"
    assert ll.head.next.next.value == "string", "Next of next of head should be 'string'"

def test_return_value():
    ll = SinglyLinkedList()
    new_head = ll.prepend(1)
    assert new_head.value == 1, "Returned node should have value 1"
    assert ll.head == new_head, "Returned node should be the new head"

def test_list_integrity_after_prepend():
    ll = SinglyLinkedList()
    ll.prepend(3)
    ll.prepend(2)
    ll.prepend(1)
    values = [1, 2, 3]
    current = ll.head
    for value in values:
        assert current.value == value, f"Expected value {value}, got {current.value}"
        current = current.next
    assert current is None, "List should end with None"

"""append()"""
def test_append_on_empty_list():
    ll = SinglyLinkedList()
    ll.append(1)
    assert ll.head.value == 1, "Head should be 1"
    assert ll.head.next is None, "Next of head should be None"

def test_append_on_non_empty_list():
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    assert ll.head.value == 1, "Head should be 1"
    assert ll.head.next.value == 2, "Next of head should be 2"

def test_append_multiple_values():
    ll = SinglyLinkedList()
    values = [1, 2, 3]
    for value in values:
        ll.append(value)
    current = ll.head
    for value in values:
        assert current.value == value, f"Expected value {value}, got {current.value}"
        current = current.next

def test_append_with_various_data_types():
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(10.5)
    ll.append("string")
    assert ll.head.value == 1, "Head should be 1"
    assert ll.head.next.value == 10.5, "Next of head should be 10.5"
    assert ll.head.next.next.value == "string", "Next of next of head should be 'string'"

def test_return_value():
    ll = SinglyLinkedList()
    new_tail = ll.append(1)
    assert new_tail.value == 1, "Returned node should have value 1"

def test_list_integrity_after_append():
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    values = [1, 2, 3]
    current = ll.head
    for value in values:
        assert current.value == value, f"Expected value {value}, got {current.value}"
        current = current.next
    assert current is None, "List should end with None"

"""insert_after_value()"""
def test_insert_after_value_on_empty_list():
    ll = SinglyLinkedList()
    ll.insert_after_value(1, 2)  # Attempt to insert '2' after '1' in an empty list
    assert ll.head is None, "List should still be empty"

def test_insert_after_value_in_list_with_single_node():
    ll = SinglyLinkedList()
    ll.append(1)
    ll.insert_after_value(1, 2)
    assert ll.head.value == 1 and ll.head.next.value == 2, "List should contain '1' followed by '2'"

def test_insert_after_value_that_exists():
    ll = SinglyLinkedList()
    for value in [1, 2, 4]:
        ll.append(value)
    ll.insert_after_value(2, 3)  # Insert '3' after '2'
    assert ll.head.next.next.value == 3, "Node with value '3' should be inserted after node with value '2'"

def test_insert_after_value_that_does_not_exist():
    ll = SinglyLinkedList()
    for value in [1, 2, 3]:
        ll.append(value)
    ll.insert_after_value(4, 5)  # Attempt to insert '5' after '4' (which does not exist)
    # Verify list integrity remains unchanged
    current = ll.head
    for expected_value in [1, 2, 3]:
        assert current.value == expected_value, f"Expected value {expected_value}, got {current.value}"
        current = current.next
    assert current is None, "List should not be modified"

def test_insert_after_value_multiple_times():
    ll = SinglyLinkedList()
    for value in [1, 2, 3]:
        ll.append(value)
    ll.insert_after_value(2, 4)
    ll.insert_after_value(4, 5)  # Insert '5' after the newly inserted '4'
    values = [1, 2, 4, 5, 3]
    current = ll.head
    for value in values:
        assert current.value == value, f"Expected value {value}, got {current.value}"
        current = current.next

def test_list_integrity_after_insertion():
    ll = SinglyLinkedList()
    values_before = [1, 2, 4, 5]
    values_after = [1, 2, 3, 4, 5]  # Expected list after insertion
    for value in values_before:
        ll.append(value)
    ll.insert_after_value(2, 3)  # Insert '3' after '2'
    current = ll.head
    for value in values_after:
        assert current.value == value, f"Expected value {value}, got {current.value}"
        current = current.next

def test_insert_after_value_with_various_data_types():
    ll = SinglyLinkedList()
    ll.append("a")
    ll.append("c")
    ll.insert_after_value("a", "b")  # Insert 'b' after 'a'
    assert ll.head.value == "a" and ll.head.next.value == "b" and ll.head.next.next.value == "c", "List should contain 'a', 'b', 'c' in order"

"""delete_by_value()"""
def test_delete_by_value_on_empty_list():
    ll = SinglyLinkedList()
    ll.delete_by_value(1)  # Attempt to delete '1' from an empty list
    assert ll.head is None, "List should remain empty after deletion attempt"

def test_delete_nonexistent_value():
    ll = SinglyLinkedList()
    for value in [1, 2, 3]:
        ll.append(value)
    ll.delete_by_value(4)  # Attempt to delete '4', which does not exist
    # Verify list integrity remains unchanged
    current = ll.head
    for expected_value in [1, 2, 3]:
        assert current.value == expected_value, f"Expected value {expected_value}, got {current.value}"
        current = current.next
    assert current is None, "List should not be modified after attempting to delete a nonexistent value"

def test_delete_only_node_in_list():
    ll = SinglyLinkedList()
    ll.append(1)
    ll.delete_by_value(1)  # Delete the only node in the list
    assert ll.head is None, "List should be empty after deleting the only node"

def test_delete_head_node():
    ll = SinglyLinkedList()
    for value in [1, 2, 3]:
        ll.append(value)
    ll.delete_by_value(1)  # Delete the head node
    assert ll.head.value == 2, "Head node should now be the one with value '2'"

def test_delete_last_node():
    ll = SinglyLinkedList()
    for value in [1, 2, 3]:
        ll.append(value)
    ll.delete_by_value(3)  # Delete the last node
    current = ll.head
    while current.next is not None:
        current = current.next
    assert current.value == 2, "Last node should now be the one with value '2'"

def test_delete_middle_node():
    ll = SinglyLinkedList()
    for value in [1, 2, 3]:
        ll.append(value)
    ll.delete_by_value(2)  # Delete a middle node
    assert ll.head.value == 1 and ll.head.next.value == 3, "Middle node should be deleted, leaving '1' and '3'"

def test_delete_node_and_return_value():
    ll = SinglyLinkedList()
    for value in [1, 2, 3]:
        ll.append(value)
    deleted = ll.delete_by_value(2)  # Assume function returns the deleted node or None
    assert deleted.value == 2, "Function should return the deleted node"
    # Verify '2' is deleted from the list
    current = ll.head
    for expected_value in [1, 3]:
        assert current.value == expected_value, f"Expected value {expected_value}, got {current.value}"
        current = current.next

if __name__ == "__main__":
    pytest.main()
