import networkx as nx
import matplotlib.pyplot as plt

graph = nx.hexagonal_lattice_graph(3,4)
cycle_basis = nx.minimum_cycle_basis(graph)

# Add nodes for the edges
i = 2000
for edge in list(graph.edges):
    graph.add_node(i)
    graph.add_edge(edge[0], i)
    graph.add_edge(edge[1], i)
    graph.remove_edge(edge[0], edge[1])
    i = i+1

# Add nodes for the tiles
i = 1000
for base in cycle_basis:
    new_tile = i
    graph.add_node(new_tile)
    for node in base:
        graph.add_edge(node, new_tile)
    i = i+1

nx.draw(graph)

plt.savefig("filename.png")