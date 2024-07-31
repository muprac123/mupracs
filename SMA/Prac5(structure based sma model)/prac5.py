import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import greedy_modularity_communities

# Step 1: Data Collection (Load the data)
# For demonstration, let's create a synthetic dataset
data = {
    'source': ['A', 'A', 'B', 'C', 'D', 'E', 'E', 'F', 'F', 'G'],
    'target': ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
}
df = pd.DataFrame(data)

# Step 2: Network Construction
G = nx.from_pandas_edgelist(df, 'source', 'target')

# Step 3: Community Detection
communities = list(greedy_modularity_communities(G))

# Add community information to nodes
community_mapping = {}
for i, com in enumerate(communities):
    for node in com:
        community_mapping[node] = i

nx.set_node_attributes(G, community_mapping, 'community')

# Step 4: Influence Analysis
pagerank = nx.pagerank(G)
nx.set_node_attributes(G, pagerank, 'pagerank')

# Step 5: Visualization
pos = nx.spring_layout(G)  # Layout for visualization
plt.figure(figsize=(12, 8))

# Draw nodes with community colors
colors = [community_mapping[node] for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=500, node_color=colors, cmap=plt.cm.jet)
nx.draw_networkx_edges(G, pos, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=12)

# Draw node labels for pagerank
pagerank_labels = {node: f'{round(rank, 2)}' for node, rank in pagerank.items()}
nx.draw_networkx_labels(G, pos, labels=pagerank_labels, font_color='red')

plt.title('Social Network with Community Detection and Influence Analysis')
plt.show()
