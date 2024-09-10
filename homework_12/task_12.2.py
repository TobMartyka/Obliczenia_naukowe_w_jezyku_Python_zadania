import networkx as nx
import matplotlib.pyplot as plt
import random

num_nodes = random.randint(6, 13)
G = nx.gnm_random_graph(num_nodes, random.randint(num_nodes, num_nodes*(num_nodes-1)//2))

plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='black', edge_color='red', node_size=500, font_size=10)
plt.title("Random nodes")
plt.show()
