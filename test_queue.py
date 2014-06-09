import pytest
import queue as q

def test_constructor():
    test = q.queue()
    assert test.head == None

def test_enqueue():
    test = q.queue()
    test.enqueue(1)
    test.enqueue(2)
    test.enqueue(3)
    assert test.dequeue() == 1
    assert test.dequeue() == 2
    assert test.dequeue() == 3

    with pytest.raises(Exception) as dequeue_empty:
        test.dequeue()
    assert dequeue_empty.value.message == 'Empty Queue!'

def test_dequeue():
    with pytest.raises(Exception) as dequeue_empty:
        test = q.queue()
        test.dequeue()
    #import pdb; pdb.set_trace()      
    assert dequeue_empty.value.message == 'Empty Queue!'
