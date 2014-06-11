import pytest
from doubly_linked_list import *

def test_constructor():
    test = DoublyLinkedList()
    assert test.head == None
    assert test.tail == None


def test_insert():
    test = DoublyLinkedList()
    test.insert(1)
    test.insert(2)
    assert test.head.val == 2
    assert test.tail.val == 1

def test_append():
    test = DoublyLinkedList()
    test.append(1)
    test.append(2)
    assert test.head.val == 1
    assert test.tail.val == 2

def test_pop():
    test = DoublyLinkedList()
    test.insert(1)
    test.insert(2)
    x = test.pop()
    assert x == 2
    assert test.head.val == 1

def test_shift():
    test = DoublyLinkedList()
    test.append(1)
    test.append(2)
    x = test.shift()
    assert x == 2
    assert test.tail.val == 1

def test_remove():
    marker = 0
    with pytest.raises(Exception) as empty_list:
        test = DoublyLinkedList()
        test.remove(1)
    assert empty_list.value.message == "currentNode is None"
    