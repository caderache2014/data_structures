class min_heap(object):
    def __init__(self):
        self.heap_list = []
        self.size = 0

    def organize_up(self,i):   
        parent_node = (i-1)//2
        while True:
            if self.heap_list[i] < self.heap_list[parent_node]:
                self.heap_list[i], self.heap_list[parent_node] = self.heap_list[parent_node], self.heap_list[i]
            i = max(parent_node,0)
            parent_node = (i-1)//2
            if i == 0:
                break

    def push(self, val):
        self.heap_list.append(val)
        self.size += 1
        self.organize_up(self.size-1)

    def pop(self):
        if self.size == 0:
            raise IndexError
        returnval = self.heap_list[0]
        self.heap_list[0] = self.heap_list[self.size-1]
        self.organize_down()
        self.size -= 1
        self.heap_list.pop(-1)
        return returnval

    def organize_down(self):
        i = 0
        left_child = (i+1)*2-1
        right_child = (i+1)*2
        if self.size == 1:
            return
        if self.size == 2:
            child_swap = 1
        else:                 
            while True:
                if self.heap_list[left_child]<=self.heap_list[right_child]:
                    child_swap = left_child
                else:
                    child_swap = right_child
                if self.heap_list[i] > self.heap_list[child_swap]:
                    self.heap_list[i], self.heap_list[child_swap] = self.heap_list[child_swap], self.heap_list[i]
                i=child_swap
                left_child = (i+1)*2-1
                right_child = (i+1)
                if right_child>=self.size-1:
                    break
    
    def peek(self):  
        return self.heap_list[0]
