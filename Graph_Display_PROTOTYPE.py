# imports
import matplotlib.pyplot as plt
import networkx as nx

# main
node_list = ["A", "B", "C", "D", "E", "F"]
edge_list = []

labels = {}

for i in range(1, len(node_list)):
    edge = (node_list[i - 1], node_list[i])
    edge_list.append(edge)

    labels[edge_list[i - 1]] = i

displayedGraph = nx.DiGraph()

displayedGraph.add_nodes_from(node_list)
displayedGraph.add_edges_from(edge_list)

pos = nx.circular_layout(displayedGraph)

plt.figure(figsize=(12, 8))

nodes = nx.draw_networkx_nodes(displayedGraph, pos, node_shape="o", node_size=12000, node_color="blue")
nx.draw_networkx_labels(displayedGraph, pos, font_color="W", font_size=11.5)
edges = nx.draw_networkx_edges(displayedGraph, pos, node_size=12000, arrowstyle="simple", arrowsize=50, edge_color="black")
nx.draw_networkx_edge_labels(displayedGraph, pos, edge_labels=labels, font_size=16)

plt.savefig("DisplayedGraph.png", format="PNG", bbox_inches="tight")
plt.show()
