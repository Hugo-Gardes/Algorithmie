import networkx as nx
from test_matching import is_matching

"""
Generates a random graph using the Erdős-Rényi model.

Parameters:
num_nodes (int): The number of nodes in the graph.
num_edges (int): The number of edges in the graph.

Returns:
networkx.Graph: A randomly generated graph.
"""


def generate_random_graph(num_nodes, num_edges):
    G = nx.gnp_random_graph(num_nodes, num_edges)
    return G


"""
Find a matching in a graph by selecting nodes with the highest degree first.
Parameters:
G (networkx.Graph): The input graph.
Returns:
list: A list of tuples representing the edges in the matching.
"""


def max_degree_matching(G):
    matching = []
    nodes = sorted(G.degree, key=lambda x: x[1], reverse=True)
    matched = set()

    for node, degree in nodes:
        if node not in matched:
            for neighbor in G.neighbors(node):
                if neighbor not in matched:
                    matching.append((node, neighbor))
                    matched.add(node)
                    matched.add(neighbor)
                    break
    return matching


"""
Find a matching in the graph G by selecting nodes with the minimum degree first.
Parameters:
G (networkx.Graph): An undirected graph.
Returns:
list: A list of tuples representing the edges in the matching.
"""


def min_degree_matching(G):
    matching = []
    nodes = sorted(G.degree, key=lambda x: x[1])
    matched = set()

    for node, _ in nodes:
        if node not in matched:
            for neighbor in G.neighbors(node):
                if neighbor not in matched:
                    matching.append((node, neighbor))
                    matched.add(node)
                    matched.add(neighbor)
                    break
    return matching
