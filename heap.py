class min_heap(object):
    def __init__(self):
        self.heap_list = []
        self.size = 0

    def organize_up(self,i):
        if i<=2:
            if self.heap_list[i] < self.heap_list[0]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[0]
                self.heap_list[0] = temp
            
        while (i-1)//2>0:
            if self.heap_list[i] < self.heap_list[(i-1)//2]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[(i-1)//2]
                self.heap_list[(i-1)//2] = temp
            i = (i-1)//2

    def push(self, val):
        self.heap_list.append(val)
        self.size += 1
        self.organize_up(self.size-1)

    def pop(self):
        if self.size == 0:
            raise IndexError
        returnval = self.heap_list[0]
        self.heap_list[0] = self.heap_list[self.size-1]
        self.size -= 1
        self.organize_down()
        return returnval

    def organize_down(self):
        i = 0
        if self.heap_list[1]<=self.heap_list[2]:
            child_swap = 1
        else:
            child_swap = 2
        if self.heap_list[0]>self.heap_list[child_swap]:
            temp = self.heap_list[0]
            self.heap_list[0] = self.heap_list[child_swap]
            self.heap_list[child_swap] = temp
        i = child_swap
                    
        while i*2+1<=self.size:
            if self.heap_list[(i+1)*2-1]<=self.heap_list[(i+1)*2]:
                child_swap = (i+1)*2-1
            else:
                child_swap = (i+1)*2
            if self.heap_list[i] > self.heap_list[child_swap]:
                temp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[child_swap]
                self.heap_list[child_swap] = temp
            i=child_swap
   
        