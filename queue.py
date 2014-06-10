class queue_item():
    def __init__(self):
        self.data = None
        self.next = None

class queue():
    def __init__(self):
        self.head= None

    def enqueue(self, data):
        new_item = queue_item()
        new_item.data = data
        new_item.next = self.head
        self.head = new_item

    def dequeue(self):
        if self.size() == 0:
            raise Exception('Empty Queue!')
        remove_item = self.head
        if not remove_item.next:
            data = remove_item.data
            self.head = None
            return data
        while remove_item.next.next:
            remove_item = remove_item.next
        data = remove_item.next.data
        remove_item.next = None
        return data

    def size(self):
        size = 0
        curr_item = self.head   
        while curr_item:
            curr_item = curr_item.next
            size += 1
        return size
        