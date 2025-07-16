def is_matching(graph, matching):
    matched_nodes = set()

    for u, v in matching:
        # Check that both nodes are part of the graph
        if u not in graph.nodes or v not in graph.nodes:
            return False

        # Check that there's an edge between u and v
        if not graph.has_edge(u, v):
            return False

        # Check that neither u nor v has been matched before
        if u in matched_nodes or v in matched_nodes:
            return False

        # Mark these nodes as matched
        matched_nodes.add(u)
        matched_nodes.add(v)

    return True
