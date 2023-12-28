# Import necessary libraries
import matplotlib.pyplot as plt
import networkx as nx

# Define the graph with edge attributes as dictionaries
graph = {
    'A': {'B': {'weight': 2}, 'C': {'weight': 3}, 'D': {'weight': 20}, 'E': {'weight': 1}},
    'B': {'A': {'weight': 2}, 'C': {'weight': 15}, 'D': {'weight': 2}, 'E': {'weight': 20}},
    'C': {'A': {'weight': 3}, 'B': {'weight': 15}, 'D': {'weight': 20}, 'E': {'weight': 13}},
    'D': {'A': {'weight': 20}, 'B': {'weight': 2}, 'C': {'weight': 20}, 'E': {'weight': 9}},
    'E': {'A': {'weight': 1}, 'B': {'weight': 20}, 'C': {'weight': 13}, 'D': {'weight': 9}}
}

# Create networkx graph from the dictionary
G = nx.from_dict_of_dicts(graph)

# Define the position of the nodes and edge labels
pos = nx.spring_layout(G) 
labels = nx.get_edge_attributes(G, 'weight')

# Draw the graph
nx.draw_networkx(G, pos, with_labels=True)

# Draw the edge labels
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Display the plot
plt.show()
