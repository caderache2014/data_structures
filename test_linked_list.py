import unittest
import linked_list as l

class ErrorTest(unittest.TestCase):

    def test_remove(self):
        test_list = l.linked_list()
        test_list.insert(1)
        test_list.insert(2)
        test_list.insert(3)
        test_list.remove(test_list.head.next.next)
        
        self.assertEqual(test_list.print_list() ,  tuple([3,2]))

if __name__ == '__main__':
    unittest.main()      

        
        
        
            
    