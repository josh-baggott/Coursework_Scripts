# imports
import matplotlib.pyplot as plt
import networkx as nx
from PIL import Image

from Graph import *


# functions


def display_graph(node_list):
    """
    This function uses an external library to create a virtual representation of the reaction pathway that has been calculated using the Graph.py script

    :param node_list: The shortest path between the start and end nodes
    :return: N/A
    """

    if not node_list:
        raise ValueError("No Route Available")

    edges = []

    labels = {}

    for i in range(1, len(node_list)):
        edge = (node_list[i - 1], node_list[i])
        edges.append(edge)

        labels[edges[i - 1]] = i

    displayedGraph = nx.DiGraph()

    displayedGraph.add_nodes_from(node_list)
    displayedGraph.add_edges_from(edges)

    pos = nx.circular_layout(displayedGraph)

    plt.figure(figsize=(12, 8))

    nx.draw_networkx_nodes(displayedGraph, pos, node_shape="o", node_size=12000, node_color="blue")
    nx.draw_networkx_labels(displayedGraph, pos, font_color="W", font_size=11.5)
    nx.draw_networkx_edges(displayedGraph, pos, node_size=12000, arrowstyle="simple", arrowsize=50, edge_color="black")
    nx.draw_networkx_edge_labels(displayedGraph, pos, edge_labels=labels, font_size=16)

    plt.savefig("DisplayedGraph.png", format="PNG", bbox_inches="tight")

    basewidth = 350
    img = Image.open('DisplayedGraph.png')
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img.save('DisplayedGraph.png')


# main


if __name__ == "__main__":

    g = ReactionGraph(startNode=input("Enter Start Node: "), endNode=input("Enter End Node: "))
    shortest_path = g.find_shortest_path()

    if not shortest_path:
        raise ValueError("No Available Route")
    else:
        display_graph(shortest_path)

    g.print_divider()

    g.display_route(shortest_path)

    print("Reaction Info: ")

    information = g.display_info(shortest_path)

    for i in range(0, len(information)):
        print(information[i])

    g.print_divider()
