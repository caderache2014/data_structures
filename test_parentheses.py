import pytest
import parentheses as p
import random
import pdb

uni1 = list(range(0x0020,0x0027))
uni2 = list(range(0x002A,0X007F))
unicomb = uni1 + uni2

def test_close_first():
    #pdb.set_trace()
    test_text = ''.join(unichr(random.choice(unicomb)) for i in range(50))
    test_text = test_text + u')'
    assert p.parentheses(test_text) == -1

def test_equal():
    num_p = random.randint(1,10)
    for i in range(num_p):
        test_text = ''.join(unichr(random.choice(unicomb)) for i in range(5))
        test_text = test_text + u'('
        test_text = test_text + ''.join(unichr(random.choice(unicomb)) for i in range(5)) 
        test_text = test_text + u')'
    #pdb.set_trace()
    assert p.parentheses(test_text) == 0

def test_more_open():
    num_p = random.randint(1,2)
    for i in range(num_p):
        test_text = '('.join(unichr(random.choice(unicomb)) for i in range(5))
        test_text = test_text + u'('
        test_text = test_text + ''.join(unichr(random.choice(unicomb)) for i in range(5)) 
        test_text = test_text + u')'
    #pdb.set_trace()
    assert p.parentheses(test_text) == 1
    

def test_more_closed():
    num_p = random.randint(1,10)
    for i in range(num_p):
        test_text = ''.join(unichr(random.choice(unicomb)) for i in range(5))
        test_text = test_text + u'('
        test_text = test_text + ''.join(unichr(random.choice(unicomb)) for i in range(5))   
        test_text = test_text + u')'
    test_text = test_text + u')'
    #pdb.set_trace()
    assert p.parentheses(test_text) == -1
