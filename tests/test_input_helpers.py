import networkx as nx

from dtool_ibeis import input_helpers


def test_dependency_subgraph_ignores_unrelated_sources():
    graph = nx.MultiDiGraph()
    graph.add_edge('relevant_a', 'middle')
    graph.add_edge('relevant_b', 'middle')
    graph.add_edge('middle', 'target')
    graph.add_edge('unrelated_source', 'unrelated_sink')

    subgraph = input_helpers._dependency_subgraph_for_target(graph, 'target')

    assert set(subgraph.nodes()) == {
        'relevant_a',
        'relevant_b',
        'middle',
        'target',
    }
    source_nodes = {node for node, degree in subgraph.in_degree() if degree == 0}
    assert source_nodes == {'relevant_a', 'relevant_b'}
