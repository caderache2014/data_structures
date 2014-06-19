import pytest
import graph as g

def test_constructor():
    test = g.graph_node('test')
    assert test.name == 'test'
    assert test.edge_list == []
    test = g.graph('graph')
    assert test.name == 'graph'
    assert test.node_dict == {}

def test_nodes():
    test = g.graph('graph')
    test.add_node('node1')
    test.add_node('node2')
    test.add_node('node3')
    assert 'node1' in test.node_dict
    assert 'node2' in test.node_dict
    assert 'node3' in test.node_dict
    assert len(test.node_dict) == 3

def test_edges():
    test = g.graph('graph')
    test.add_edge('node1','node2')
    test.add_edge('node1','node3')
    test.add_edge('node2','node3')
    assert test.edges() == set([frozenset(['node1','node2']),
                                frozenset(['node1','node3']),
                                frozenset(['node2','node3'])])

def test_del_node():
    test = g.graph('graph')
    test.add_edge('node1','node2')
    test.add_edge('node1','node3')
    test.add_edge('node2','node3')
    test.add_edge('node3','node4')
    test.del_node('node3')
    assert 'node1' in test.node_dict
    assert 'node2' in test.node_dict
    assert 'node4' in test.node_dict
    assert len(test.node_dict) == 3
    assert test.edges() == set([frozenset(['node1','node2'])])
    with pytest.raises(ValueError):
        test.del_node('node3')
    
    
def test_has_node():
    test = g.graph('graph')
    test.add_node('node1')
    test.add_node('node2')
    assert test.has_node('node1')
    assert test.has_node('node2')
    assert not test.has_node('node3')

def test_neighbors():
    test = g.graph('graph')
    test.add_edge('node1','node2')
    test.add_edge('node1','node3')
    assert set(test.neighbors('node1')) == set(['node2','node3'])

def test_adjacent():
    test = g.graph('graph')
    test.add_edge('node1','node2')
    test.add_edge('node1','node3')
    assert test.adjacent('node1','node2')
    assert test.adjacent('node1','node3')
    assert not test.adjacent('node2','node3')
    with pytest.raises(ValueError):
        test.adjacent('node1','node4')
                               