class node:
    def __init__(self):
        self.data = None 
        self.next = None 


class linked_list:
    def __init__(self):
        self.head= None

    def insert(self, data):
        new_node = node() 
        new_node.data = data
        new_node.next = self.head 
        self.head = new_node 

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
        #temp = node
        startnode = self.head
        while startnode.next != node:
            startnode = startnode.next
        startnode.next = startnode.next.next
        #if node.next:
            #node.data = node.next.data
            #node.next = node.next.next
        #else:
            #node.data = None
            #node = None
        #del temp
        
    def print_list(self):
        result_list = []
        node = self.head
        while node:
            result_list.append(node.data)
            node = node.next
        return tuple(result_list)
        
        
        
        
    
        