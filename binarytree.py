class node(object):
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

class binary_tree(object):
    def __init__(self, name, root):
        self.name = name
        self.root = node(root)
        self.depth_max = 0
        self.depth_curr = 0

    def insert(self, val, parent=self.root):
        new_node = node(val)
        if val<parent.value:
            if parent.left_child:
                insert(val, parent.left_child):
            else:
                parent.left_child = new_node
        else:
            if parent.right_child:
                insert(val, parent.right_child):
            else:
                parent.right_child = new_node

    def traverse(self, curr_node=self.root):
        if curr_node.left_child:
            self.depth_curr += 1
            traverse(curr_node.left_child)
        else:
            self.depth_max=max(self.depth_max,self.depth_curr)
            self.curr_depth -= 1
            traverse(curr_node.right_child)

    


        
            
        
