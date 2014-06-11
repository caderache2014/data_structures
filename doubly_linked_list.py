class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, head = None):
        self.head = head
        self.tail = head

    def insert(self, val):
        new_node = Node(val)
        if (self.tail is None):
            self.tail = new_node
            self.head = self.tail
        elif (self.head == self.tail):
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.tail = new_node.next
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node


    def append(self, val):
        new_node = Node(val)
        if (self.head is None ):
            self.head = new_node
            self.tail = self.head
        elif (self.head == self.tail):
            new_node.next = None
            new_node.prev = self.head
            self.head.next = new_node
            self.tail = new_node
        else:
            new_node.next = None
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        val = self.head.val
        self.head = self.head.next
        self.head.prev = None
        return val

    def shift(self):
        val = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None
        return val

    def remove(self, val):
        currentNode = self.head
        if currentNode is None:
            raise Exception("currentNode is None")
        while (currentNode.val != val):
            currentNode = currentNode.next
            if (currentNode is None):
                raise Exception("currentNode is None")
        currentNode.prev.next = currentNode.next
        currentNode.next.prev = currentNode.prev
         