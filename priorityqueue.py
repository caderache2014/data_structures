import heap as h

class priorityqueue(h.min_heap):
    def __init__(self):
        super(priorityqueue, self).__init__()
        self.items = {}
    def insert(self, priority, val):
        if priority in self.items:
            self.items[priority].append(val)
        else:
            self.items[priority] = [val]
        self.push(priority)

    def pop(self):
        priority = super(priorityqueue, self).pop()
        return self.items[priority].pop(0)

    def peek(self):
       return super(priorityqueue, self).peek()

