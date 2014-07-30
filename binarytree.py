class node(object):
    def __init__(self, key, left_child=None, right_child=None, parent=None):
        self.key = key
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def hasLeftChild(self):
        return self.left_child

    def hasRightChild(self):
        return self.right_child

    def isLeftChild(self):
        return self.parent and self.parent.left_child == self

    def isRightChild(self):
        if self.parent and self.parent.right_child == self:
            return True
        else:
            return False

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right_child or self.left_child)

    def hasAnyChildren(self):
        if self.right_child or self.left_child:
            return True
        else:
            return False

    def hasBothChildren(self):
        if self.right_child and self.left_child:
            return True
        else:
            return False

    def replaceNodeData(self, key, lc, rc):
        self.key = key
        self.left_child = lc
        self.right_child = rc
        if self.hasLeftChild():
            self.left_child.parent = self
        if self.hasRightChild():
            self.right_child.parent = self
    """
    Helper methods for Deletion
    """
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.findSuccessor()
                    self.parent.right_child = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.left_child
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left_child = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
                if self.hasLeftChild():
                    if self.isLeftChild():
                            self.parent.left_child = self.left_child
                    else:
                            self.parent.right_child = self.left_child
                            self.left_child.parent = self.parent
                else:
                    if self.isLeftChild():
                        self.parent.left_child = self.right_child
                    else:
                        self.parent.right_child = self.right_child
                        self.right_child.parent = self.parent

    #iteration defined for in-order traversal
    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for element in self.left_child:
                    yield element
            yield self.key
            if self.hasRightChild():
                for element in self.right_child:
                    yield element

    def __getitem__(self, key):
        return self.key


class binary_tree(object):
    def __init__(self, key):
        self.root = node(key)
        self.depth_max = 1
        self.depth_curr = 1
        self.size = 1

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    # def __iter__(self):
    #     return self.root.__iter__()

    def __setitem__(self, key, val):
        self.put(key, val)


    # def insert(self, val, parent=self.root):
    #     new_node = node(val)
    #     if val<parent.value:
    #         if parent.left_child:
    #             insert(val, parent.left_child)
    #         else:
    #             parent.left_child = new_node
    #     else:
    #         if parent.right_child:
    #             insert(val, parent.right_child)
    #         else:
    #             parent.right_child = new_node

    """
    WIth put method defined we can overload the [] operator for assignment by having the
    __setitem__ method call the put method. This allows us to  write Python statements like 
    myZipCodeTree['Seattle'] = 98101 like a dictionary
    """
    def put(self, key):
        if self.root:
            self._put(key, self.root)
        else:
            self.root = node(key)
        self.size = self.size + 1

    def _put(self, key, currentNode):
        if key < currentNode.key:
                if currentNode.hasLeftChild():
                    self._put(key, currentNode.left_child)
                else:
                    currentNode.left_child =node(key, parent=currentNode)
        else:
                if currentNode.hasRightChild():
                    self._put(key, currentNode.rightChild)
                else:
                    currentNode.rightChild = node(key, parent=currentNode)

    """
    Get methods to retrieve a value for  a given key
    By implementing the __getitem__ method we can write a Python statement
    that looks like we are accessing a dictionary. For example, we can write
    z = myZipCodeTree['Seattle'] and get '98101' for 'z'.
    """
    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.key
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.left_child)
        else:
            return self._get(key, currentNode.right_child)

    def __getitem__(self, key):
        return self.get(key)

    """
    By implementing get, we can use the 'in' operation by writing a __contains__ method for the BST.
    The __contains__ method will simply call get and return True if get returns a value, or False,
    if it returns None.
    """
    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False


    """
    Deletion methods
    """
    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in my tree')
        elif self.size == 1 and self.root.key == key:
            self.root  = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.left_child:
                currentNode.parent.left_child = None
            else:
                currentNode.parent.right_child = None
        elif currentNode.hasBothChildren():
            succ  = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
        else:
            #this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.left_child.parent = currentNode.parent
                    currentNode.parent.left_child = currentNode.left_child
                elif currentNode.isRightChild():
                    currentNode.left_child.parent = currentNode.parent
                    currentNode.parent.right_child = currentNode.left_child
                else:
                    currentNode.replaceNodeData(currentNode.left_child.key,
                                                                    currentNode.left_child.key,
                                                                    currentNode.left_child.left_child,
                                                                    currentNode.left_child.right_child)
            else:
                if currentNode.isLeftChild():
                    currentNode.right_child.parent = currentNode.parent
                    currentNode.parent.left_child.currentNode.right_child
                elif currentNode.isRightChild():
                    currentNode.right_child.parent = currentNode.parent
                    currentNode.parent.right_child = currentNode.right_child
                else:
                    currentNode.replaceNodeData(currentNode.right_child.key,
                                                                        currentNode.right_child.payload,
                                                                        currentNode.right_child.left_child,
                                                                        currentNode.right_child.right_child)

   

    """
    Travsersals: in-order, pre-order, post-order, and level-order
    """
    # def traversal(self, curr_node=self.root):
    #     if curr_node.left_child:
    #         self.depth_curr += 1
    #         traverse(curr_node.left_child)
    #     else:
    #         self.depth_max=max(self.depth_max,self.depth_curr)
    #         self.curr_depth -= 1
    #         traverse(curr_node.right_child)

    def level_order(self): #Breadth-First Traversal
        q = []
        if self.root:
            q.append(self.root)
        else:
            return
        while q:
            node = q.pop(0)
            yield node
            if node.left_child is not None:
                q.append(node.left_child)
            if node.right_child is not None:
                q.append(node.right_child)
    
    def inorder(self):
        parent_stack = []
        node = self.root
        while parent_stack or node is not None:
            if node is not None:
                parent_stack.insert(0, node)
                node = node.left_child
            else:
                node = parent_stack.pop(0)
                yield node
                node = node.right_child

    

    def preorder(self):
        return self._pre_order(self.root)

    def _pre_order(self, node):
        if node:
            yield node.key
            for left_subtree_value in self._pre_order(node.left_child):
                yield left_subtree_value
            for right_subtree_value in self._pre_order(node.right_child):
                yield right_subtree_value

           

    def postorder(self):
            parent_stack = []
            last_node = None
            node = self.root
            while parent_stack or node is not None:
                if node is not None:
                    parent_stack.insert(0, node)
                    node = node.left_child
                else:
                    peek_node = parent_stack[0]
                    if peek_node.right_child is not None and last_node is not peek_node.right_child:
                        node = peek_node.right_child
                    else:
                        parent_stack.pop(0)
                        yield peek_node
                        last_node = peek_node

        
            
        
