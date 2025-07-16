import networkx as nx
from test_matching import is_matching
import time
import statistics
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt


def generate_random_graph(num_nodes, num_edges):
    G = nx.gnp_random_graph(num_nodes, num_edges)
    return G


n, p = 120, 0.04


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


num_trials = 1400
max_degree_sizes = []
min_degree_sizes = []
max_degree_times = []
min_degree_times = []
mean_degree_min_size = []
mean_degree_max_size = []

for _ in range(num_trials):
    G = generate_random_graph(n, p)

    start_time = time.time()
    max_degree_match = max_degree_matching(G)
    max_degree_times.append(time.time() - start_time)
    max_degree_sizes.append(len(max_degree_match))

    start_time = time.time()
    min_degree_match = min_degree_matching(G)
    min_degree_times.append(time.time() - start_time)
    min_degree_sizes.append(len(min_degree_match))
    mean_degree_min_size.append(statistics.mean(min_degree_sizes))
    mean_degree_max_size.append(statistics.mean(max_degree_sizes))

print("Max Degree Matching - Average Size:", statistics.mean(max_degree_sizes))
print(f"Max Degree Matching - Average Time: {statistics.mean(max_degree_times):.5f}")
print("Min Degree Matching - Average Size:", statistics.mean(min_degree_sizes))
print(f"Min Degree Matching - Average Time: {statistics.mean(min_degree_times):.5f}")

with PdfPages("../pdf/comparison_results.pdf") as pdf:
    plt.figure()
    plt.plot(max_degree_sizes, label="Max Degree Sizes")
    plt.plot(min_degree_sizes, label="Min Degree Sizes")
    plt.title("Matching Size Distribution")
    plt.xlabel("Trial")
    plt.ylabel("Size")
    plt.legend()
    pdf.savefig()
    plt.close()

    plt.figure()
    plt.plot(max_degree_times, label="Max Degree Times")
    plt.plot(min_degree_times, label="Min Degree Times")
    plt.title("Matching Time Distribution")
    plt.xlabel("Trial")
    plt.ylabel("Time (seconds)")
    plt.legend()
    pdf.savefig()
    plt.close()

    plt.figure()
    plt.plot(mean_degree_max_size, label="Max Degree Times")
    plt.plot(mean_degree_min_size, label="Min Degree Times")
    plt.title("Matching mean size Distribution")
    plt.xlabel("Trial")
    plt.ylabel("Mean")
    plt.legend()
    pdf.savefig()
    plt.close()
