# imports
import json


# classes
class ReactionGraph:

    def __init__(self, startNode=None, endNode=None):
        if startNode:
            self.startNode = startNode
        if endNode:
            self.endNode = endNode

        self.Graph = self.open_graph()
        self.reactions = self.open_reactions()

    # setter & getter methods
    @property
    def startNode(self):
        return self.__startNode

    @startNode.setter
    def startNode(self, startNode):
        self.__startNode = startNode

    @property
    def endNode(self):
        return self.__endNode

    @endNode.setter
    def endNode(self, endNode):
        self.__endNode = endNode

    # functions
    def open_graph(self):
        """
        This function opens the JSON file Graph.json as a dictionary so it can be easily accessed by the program.

        :return: A dictionary created from Graph.json
        """

        with open("Graph.json") as json_file:
            self.Graph = json.load(json_file)

        return self.Graph

    def open_reactions(self):
        """
        This function opens the JSON file Reactions_JSON.json as a dictionary so it can be easily accessed by the program.

        :return: A dictionary created from Reactions_JSON.json
        """

        with open("Reactions_JSON.json") as json_file:
            self.reactions = json.load(json_file)

        return self.reactions

    def find_shortest_path(self, start=None, end=None, path=[]):
        """
        This function takes the starting node and the destination node and tries to plot the shortest route between them. It also checks the
        users inputs to check to see whether or not they are in the graph.

        :param graph: A graph linking the different chemical compounds (nodes) to each other via edges which represent chemical reactions
        :param start: The node where the traversal starts from
        :param end: The node where the algorithm tries to traverse to
        :param path: The shortest path between the two nodes
        :return: path (see above)
        """

        if start:
            self.startNode = start
        if end:
            self.endNode = end

        path = path + [self.startNode]
        new_path = ""

        if self.startNode not in self.Graph and self.endNode not in self.Graph:
            raise ValueError("Both Nodes Entered Incorrectly")
        elif self.startNode not in self.Graph:
            raise ValueError("Start Node Entered Incorrectly")
        elif self.endNode not in self.Graph:
            raise ValueError("End Node Entered Incorrectly")

        if self.startNode == end:
            return path

        shortest = None

        for node in self.Graph[self.startNode]:
            if node not in path:
                new_path = self.find_shortest_path(node, self.endNode, path)

            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path

        if shortest is None:
            return False

        return shortest

    def display_info(self, graph_route):
        """
        This function obtains the lists holding the info about each reaction from the dictionary reactions and displays each of them. The
        lists are obtained by combining consecutive elements in the graph_route list.

        :param graph_route: The route plotted between the start and end nodes
        :return: A list of the information of each reaction to be displayed
        """

        reactions = []

        for node in range(1, len(graph_route)):
            reactions.append(str(graph_route[node - 1]) + " \N{RIGHTWARDS ARROW} " + str(graph_route[node]))

        return reactions

    def print_divider(self):
        """
        This procedure prints a divider which separates out the inputs and the outputs, making them easier to distinguish

        :return: N/A
        """

        print("")
        print("****************************************************************************************************************************************************")
        print("")


# main
if __name__ == "__main__":
    g = ReactionGraph(startNode=input("Enter Start Node: "), endNode=input("Enter End Node: "))

    g.print_divider()

    route = g.find_shortest_path()

    # g.display_route(route)

    reaction_list = g.display_info(route)

    print(reaction_list)

    g.print_divider()
