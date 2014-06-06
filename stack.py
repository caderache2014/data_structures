class stackitem:
    def __init__(self):
        self.data = None 
        self.next = None 

class stack:
    def __init__(self):
        self.head= None

    def push(self, data):
        new_stackitem = stackitem() 
        new_stackitem.data = data
        new_stackitem.next = self.head 
        self.head = new_stackitem

    def pop(self):
        if self.head == None:
            raise Exception('Popping empty stack')
        data = self.head.data
        self.head = self.head.next
        return data
