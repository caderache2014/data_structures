import pytest
import priorityqueue as pq

def test_constructor():
    test = pq.priorityqueue()
    assert test.items == {}

def test_insert():
    test = pq.priorityqueue()
    test.insert(1, "hello")
    test.insert(2, "I")
    test.insert(3, "am")
    test.insert(4, "in")
    test.insert(5, "order")
    result = ''
    keys = sorted(test.items.keys())
    for k in keys:
        result = result + test.items[k][0] 
    result = result.strip()
    assert result == "helloIaminorder"


def test_pop():
    test = pq.priorityqueue()
    test.insert(1, "hello")
    test.insert(2, "I")
    test.insert(3, "am")
    test.insert(4, "in")
    test.insert(5, "order") 
    val = test.pop()
    assert val == "hello"
    val = test.pop()
    assert val == "I"
    val = test.pop()
    assert val == "am"
    val = test.pop()
    assert val == "in"
    val = test.pop()
    assert val == "order"

def test_peek():
    test = pq.priorityqueue()
    test.insert(6, "six")
    retval = test.peek()
    assert retval == 6

def test_multivalues():
    test = pq.priorityqueue()
    test.insert(1, "first")
    test.insert(1, "second")
    return test.pop()