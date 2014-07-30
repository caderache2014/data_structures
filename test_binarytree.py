import pytest
from binarytree import binary_tree as bst
from binarytree import node as node

"""
Test Tree Node Class
"""
def test_node_constructor():
    n = node(1)
    assert n.key== 1
    assert n.left_child== None
    assert n.right_child == None
    assert n.parent == None

def  test_hasRightChild():
    n =  node(1, right_child  = node(2))
    assert n.right_child and n.right_child.key == 2

def test_hasLeftChild():
    n = node(1, left_child = node(0))
    assert n.left_child and n.left_child.key == 0

def test_isRightChild():
    tree = bst(2)
    tree.put(3)
    n = tree._get(3, tree.root)
    assert  n.isRightChild() == True

def test_isLeftChild():
    tree = bst(2)
    tree.put(1)
    n = tree._get(1, tree.root)
    assert  n.isLeftChild() == True

def test_isRoot():
    root = node(1)
    assert root.isRoot() == True


def test_hasAnyChildren():
    root = node(1, right_child=node(2))
    assert root.hasAnyChildren() == True
    root = node(2, left_child=node(1))
    assert root.hasAnyChildren() == True

def test_hasBothChildren():
    root = node(2, right_child=node(3), left_child=node(1))
    assert root.hasBothChildren() == True

def test_replaceNodeData():
    left = node(1)
    right = node(3)
    root = node(2)

    assert root.key == 2
    assert root.isLeaf() == True
    assert left.parent == None and right.parent == None
    
    root.replaceNodeData(2.1, left, right)
    assert  root.key == 2.1
    assert left.parent == root
    assert right.parent == root

def test_findSuccessor():
    tree = bst(5)
    tree.put(2)
    tree.put(3)
    tree.put(10)
    tree.put(7)
    node3 = tree._get(3, tree.root)
    node5 = tree._get(5, tree.root)
    assert node3.findSuccessor() == node5


def  test_findMin():
    tree = bst(5)
    tree.put(4)

    minNode = tree.root.findMin()
    assert minNode.key == 4


def test_spliceOut():
    tree = bst(5)
    tree.put(4)
    tree.put(6)
    tree.put(1)
    tree.put(4.5)
    #try to spliceOut node4
    node4 = tree._get(4, tree.root)
    node4.spliceOut()
    assert tree.root.left_child.key == 1


"""
Test Binary Search Tree Class
"""
def test_tree_constructor(): 
    tree = bst(5)
    assert tree.get(5) == tree.root.key
    assert tree.depth_max == 1

def  test_tree_length():
    root = node(5)
    tree = bst(root)
    tree.put(4)
    tree.put(6)
    tree.put(1)
    tree.put(4.5)
    assert tree.length() == 5

def test_put():
    tree = bst(5)
    assert tree.length() == 1

    tree.put(4)
    assert tree.length() == 2

def test_get():
    tree = bst(5)
    root = tree.get(5)

    assert root == 5

def test_delete():
    tree = bst(5)
    tree.delete(5)

    assert tree.root == None

def test_remove():
    tree = bst(5)
    tree.put(4)
    nodeToRemove = tree._get(4, tree.root)
    tree.remove(nodeToRemove)
    assert tree.root.isLeaf() == True

def test_level_order():
    a = [3, 1, 6, 4, 7, 10, 14, 13]
    tree = bst(8)
    for i in a:
        tree.put(i)
    
    assert tree.level_order() == [8, 3, 1, 10, 6, 14, 4, 7, 13]

def test_inorder():
    a = [3, 1, 6, 4, 7, 10, 14, 13]
    tree = bst(8)
    for i in a:
        tree.put(i)
    out = tree.inorder()
    assert [key for key in out] == [1, 3, 10, 1, 6, 14, 4, 7, 13]

def test_postorder():
    a = [3, 1, 6, 4, 7, 10, 14, 13]
    tree = bst(8)
    for i in a:
        tree.put(i)
    assert tree.postorder() == [8, 3, 10, 1, 6, 14, 4, 7, 13]


def test_preorder():
    tree = optimal_bst()
    expected = [2, 5, 4, 7, 9, 8, 6]
    actual = [i for i in tree.preorder()]
    assert actual == expected

def optimal_bst():
    input = [4, 8, 2, 5, 7, 9]
    tree = bst(6)
    for i in input:
        tree.put(i)
    return tree