import pytest
import heap as h

def test_constructor():
    test = h.min_heap()
    assert test.heap_list == []
    assert test.size == 0

def test_push():
    test = h.min_heap()
    test.push(1)
    test.push(10)
    test.push(20)
    test.push(5)
    assert test.heap_list[0] == 1
    assert test.heap_list[1] == 5
    assert test.heap_list[2] == 20  
    assert test.heap_list[3] == 10

def test_pop():
    test = h.min_heap()
    test.push(1)
    test.push(30)
    test.push(29)
    test.push(100)

    assert test.pop() == 1
    assert test.pop() == 29
    assert test.pop() == 30
    assert test.pop() == 100
    with pytest.raises(IndexError):
        test.pop()
    
