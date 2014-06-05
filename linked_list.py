#! /usr/bin/env python

class node:
    def __init__(self, val = None):
        self.data = val #contains data
        self.next = None #contains reference to next node


class linked_list:
    def __init__(self, head = None):
        self.head = None

    def insert(self, data):
        new_node = node()  #create a new node
        new_node .data = data
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
         node = self.head
         result_list = []
         while node:
            result_list.append(node.data)
            node = node.next
         print  tuple(result_list)
         return tuple(result_list)

    def pop(self):
        data = self.head.data
        self.head = self.head.next
        return data

    def size(self):
        node = self.head
        size = 0
        while node:
            size = size + 1
            node = node.next
        return size

    def search(self, val):
        node = self.head
        while node:
            if node.data == val:
                return node
            node = node.next
        return None

    def remove(self, node):
        if node.next:
            node.data = node.next.data
            node.next = node.next.next
        elif not self.head.next and node.data == self.head.data:
            print "Self head next is %s"  %  self.head.next
            self.head = None
        else: 
            runner = self.head
            runnerNext = self.head.next
            while runnerNext:
                if runnerNext.data == node.data:
                    runner.next = runnerNext.next
                    break
                runner = runner.next
                runnerNext = runnerNext.next


        
