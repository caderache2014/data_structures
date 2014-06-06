import pytest
import stack as s

def test_constructor():
    test = s.stack()
    assert test.head == None

def test_push():
    test = s.stack()
    test.push(1)
    test.push(2)
    test.push(3)
    assert test.pop() == 3
    assert test.pop() == 2
    assert test.pop() == 1
    

def test_pop():
    with pytest.raises(Exception) as popempty:
        test = s.stack()
        test.pop()
    #import pdb; pdb.set_trace()      
    assert popempty.value.message == 'Popping empty stack'
