
import unittest
from linked_list import  linked_list
from linked_list import node

class PositiveUnitTest(unittest.TestCase):

        #knownvalues
        #insert
        def testInsert(self):
            """insert should give a known result with known input"""
            item = 5
            l1 = linked_list()
            l1.insert(item)
            x = l1.print_list()
            y = tuple([5])
            self.assertEqual(x, y)


        #pop
        def testPop(self):
            """pop should give a known result with a known input"""
            item1 = 5
            item2 = 10
            l2 = linked_list()
            l2.insert(item1)
            l2.insert(item2)
            x = l2.pop()
            self.assertEqual(x, item2)
            self.assertEqual(1, l2.size())


        #print_list
        def testPrint(self):
            item1 = 5
            item2 = 10
            item3 = "three"
            l3 = linked_list()
            l3.insert(item1)
            l3.insert(item2)
            l3.insert(item3)
            x = l3.print_list()
            y = tuple(["three", 10, 5])
            self.assertEqual(x, y)

        #remove head from list of size 2
        def testRemove2(self):
             lst = linked_list()
             lst.insert(1)
             lst.insert(2)
             short_list = lst.remove(lst.head)
             x = lst.print_list()
             self.assertEqual(x, tuple([1]))

        #remove head from a llist of size == 1
        def testRemoveSingle(self):
            lst = linked_list()
            lst.insert(1)
            lst.remove(lst.head)
            self.assertEqual(None, lst.head)

        #remove head from a  list with size > 2
        def testRemove3(self):
            lst = linked_list()
            lst.insert(1)
            lst.insert(2)
            lst.insert(3)
            lst.remove(lst.head)
            self.assertEqual(tuple([2, 1]), lst.print_list())


        #search
        def testSearch(self):
            item = 1
            ls2 = linked_list()
            ls2.insert(item)
            nd2 = ls2.search(item)
            self.assertEqual(nd2.data, item)


class NegativeUnitTest(unittest.TestCase):
        #insert a value and it's size is not False
        def testInsert(self):
            lst = linked_list()
            lst.insert(1)
            self.assertFalse(0, lst.size())

            #test printing an empty list
        def testPrint(self):
            lst = linked_list()
            self.assertFalse(0, lst.print_list())

            #test that a singleton list, popped, is now empty
        def testPop(self):
            lst = linked_list()
            lst.insert(1)
            lst.pop()
            self.assertFalse(False, lst.size())

        #test that removing the head does not  create false data    
        def testRemove(self):
            lst = linked_list()
            lst.insert(1)
            lst.insert(2)
            lst.insert(3)
            lst.insert(4)
            lst.remove(lst.head.next)
            self.assertFalse(0, lst.head.data)

        #search for an absent value returns None
        def testSearch(self):
            lst = linked_list()
            lst.insert(1)
            lst.insert(2)
            lst.insert(3)
            lst.insert(4)
            lst.insert(5)
            x = lst.search(7)
            self.assertFalse(0, x)


if __name__ == "__main__":
    unittest.main()
