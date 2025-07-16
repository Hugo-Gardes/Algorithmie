# EX2.PY Documentation

This script performs a comparison between two graph matching algorithms: max-degree matching and min-degree matching. It generates random graphs, applies both matching algorithms, and records their performance in terms of size and execution time. The results are then plotted and saved to a PDF file.

## Functions

### `generate_random_graph(num_nodes, num_edges)`
Generates a random graph using the Erdős-Rényi model.
- **Parameters:**
    - `num_nodes` (int): Number of nodes in the graph.
    - `num_edges` (float): Probability for edge creation.
- **Returns:**
    - `G` (networkx.Graph): A randomly generated graph.

### `max_degree_matching(G)`
Finds a matching in the graph by prioritizing nodes with the highest degree.
- **Parameters:**
    - `G` (networkx.Graph): The input graph.
- **Returns:**
    - `matching` (list of tuples): List of matched node pairs.

### `min_degree_matching(G)`
Finds a matching in the graph by prioritizing nodes with the lowest degree.
- **Parameters:**
    - `G` (networkx.Graph): The input graph.
- **Returns:**
    - `matching` (list of tuples): List of matched node pairs.

## Variables

- `n` (int): Number of nodes in the graph.
- `p` (float): Probability for edge creation.
- `num_trials` (int): Number of trials to run for each matching algorithm.
- `max_degree_sizes` (list): Sizes of matchings found by the max-degree algorithm.
- `min_degree_sizes` (list): Sizes of matchings found by the min-degree algorithm.
- `max_degree_times` (list): Execution times for the max-degree algorithm.
- `min_degree_times` (list): Execution times for the min-degree algorithm.
- `mean_degree_min_size` (list): Mean sizes of matchings found by the min-degree algorithm over trials.
- `mean_degree_max_size` (list): Mean sizes of matchings found by the max-degree algorithm over trials.

## Execution

The script runs `num_trials` trials, generating a random graph for each trial and applying both matching algorithms. It records the size and execution time for each trial. After all trials, it prints the average size and execution time for both algorithms. Finally, it plots the size and time distributions and saves them to a PDF file.

## Output

- Printed average size and execution time for both matching algorithms.
- A PDF file (`comparison_results.pdf`) containing plots of the size and time distributions for both algorithms.