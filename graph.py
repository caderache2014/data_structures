from functools import total_ordering

@total_ordering
class graph_node(object):
    def __init__(self, name):
        self.name = name
        self.edge_list = []
        
    def add_node_edge(self, *edges):
        for item in edges:
            if item not in self.edge_list:
                self.edge_list.append(item)

    def __eq__(self, other):
        if self.name == other.name:
            return set(self.edge_list) == set(other.edge_list)
        return False

    def __ne__(self, other):
        return not __eq__(self, other)

    def __lt__(self, other):
        return len(self.edge_list) > len(other.edge_list)
    
class graph_edge(object):
    def __init__(self, node1, node2):
        self.end_points = frozenset([node1.name,node2.name])

class graph(object):
    def __init__(self, name):
        self.name = name
        self.node_dict = {}

    def nodes(self):
        return list(self.node_dict.keys())

    def edges(self):
        edge_list = []
        for keys in self.node_dict:
            for edge in self.node_dict[keys].edge_list:
                edge_list.append(edge.end_points)
        return set(edge_list)

    def add_node(self, n):
        if self.has_node(n):
            raise NameError
        self.node_dict[n]=graph_node(n)

    def add_edge(self,n1,n2):
        if self.has_node(n1) and not self.has_node(n2):
            self.node_dict[n2] = graph_node(n2)
        elif self.has_node(n2) and not self.has_node(n1):
            self.node_dict[n1] = graph_node(n1)
        elif not self.has_node(n1):
            self.node_dict[n2] = graph_node(n2)
            self.node_dict[n1] = graph_node(n1)
        self._attach_edge(n1,n2)

    def del_node(self,n):
        if not self.has_node(n):
            raise ValueError
        for keys in self.node_dict:
            if self.adjacent(self.node_dict[keys].name,n):
                self.del_edge(self.node_dict[keys].name,n)
        del self.node_dict[n]

    def del_edge(self, n1, n2):
        check_edge = graph_edge(self.node_dict[n1],self.node_dict[n2])
        if self.adjacent(n1,n2):
            for index, item in enumerate(self.node_dict[n1].edge_list):
                if check_edge.end_points == item.end_points:
                    break
            del self.node_dict[n1].edge_list[index]
            #print self.node_dict[n1].edge_list[i]
            for index, item in enumerate(self.node_dict[n2].edge_list):
                if check_edge.end_points == item.end_points:
                    break
            del self.node_dict[n2].edge_list[index]
            #print self.node_dict[n1].edge_list[i]
        else:
            raise ValueError

    def has_node(self, n):
        return n in self.node_dict

    def neighbors(self, n):
        neighbor_list = []
        if not self.has_node(n):
            raise ValueError
        if self.node_dict[n].edge_list == []:
            return
        for item in self.node_dict[n].edge_list:
            neighbor_list = neighbor_list + list(item.end_points)
        neighbor_list = list(set(neighbor_list))
        i = neighbor_list.index(self.node_dict[n].name)
        del neighbor_list[i]
        return neighbor_list

    def adjacent(self, n1,n2):
        if n1 == n2:
            return False
        if not self.has_node(n1) or not self.has_node(n2):
            raise ValueError
        check_edge = graph_edge(self.node_dict[n1],self.node_dict[n2])
        for edge in self.node_dict[n1].edge_list:
            if check_edge.end_points == edge.end_points:
                return True
        for edge in self.node_dict[n2].edge_list:
            if check_edge.end_points == edge.end_points:
                return True
        return False
 
    def _attach_edge(self, n1,n2):
        new_edge = graph_edge(self.node_dict[n1],self.node_dict[n2])
        self.node_dict[n1].add_node_edge(new_edge)
        self.node_dict[n2].add_node_edge(new_edge)

if __name__ == '__main__':
    g = graph('graph')
    g.add_node('node1')
    print g.nodes()
    print g.edges()
    g.add_edge('node1','node2')
    g.add_edge('node1','node3')
    g.add_edge('node2','node3')
    print g.nodes()
    print g.edges()
    g.del_node('node3')
    print g.edges()
    print g.neighbors('node1')
    
    