import networkx as nx
import matplotlib.pyplot as plt

# Sample data (replace with your own data)
edges = [("user1", "user2"), ("user1", "user3"), ("user2", "user3"), ("user2", "user4")]

# Create a directed graph
G = nx.DiGraph()

# Add edges to the graph
G.add_edges_from(edges)

# Visualize the network
nx.draw(G, with_labels=True)
plt.show()

# Calculate degree centrality
degree_centrality = nx.degree_centrality(G)
print("Degree Centrality:", degree_centrality)

# Calculate betweenness centrality
betweenness_centrality = nx.betweenness_centrality(G)
print("Betweenness Centrality:", betweenness_centrality)
