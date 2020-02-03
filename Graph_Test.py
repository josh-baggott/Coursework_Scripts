# imports
import unittest

from Graph import *


# classes
class TestMethods(unittest.TestCase):

    # functions
    def test_find_shortest_path(self):
        """
        Tests for the function find_shortest_path in the script Graph.py

        :return: N/A
        """

        self.assertEqual(g.find_shortest_path(start="Carboxylic Acid", end="Ketone"), ["Carboxylic Acid", "Alcohol", "Ketone"])
        # Short Route OK - I chose this route as compared to most routes on this graph, it is one of the shorter ones

        self.assertEqual(g.find_shortest_path(start="Carboxylic Acid", end="Tertiary Alcohol"), ["Carboxylic Acid", "Alcohol", "Halogenoalkane", "Grignard Reagent", "Tertiary Alcohol"])
        # Long Route OK - I chose this route as compared to most routes on this graph, it is one of the longer ones so there is a larger probability of an error

        self.assertFalse(g.find_shortest_path(start="Amine", end="Alcohol"))
        # No Route Between Points - I chose to test this as this would be quite a common occurrence since the user is unable to see the graph and may not remember how to get from one compound to another

        self.assertRaises(ValueError, g.find_shortest_path, "Carboxillic Acid", "Ketone")
        # Start Node Spelt Incorrectly - I chose this spelling error because this is one of the more common ones as it is so similar to the correct spelling. This could result in the program mixing them up and throwing an error

        self.assertRaises(ValueError, g.find_shortest_path, "Carboxylic Acid", "Keton")
        # End Node Spelt Incorrectly - I chose this spelling error because this is one of the more common ones as it is so similar to the correct spelling. This could result in the program mixing them up and throwing an error

        self.assertRaises(ValueError, g.find_shortest_path, "Carboxyllic Acid", "Keton")
        # Both Nodes Spelt Incorrectly - I chose these spelling error because as stated previously these are two of the more common ones as they are so similar to the correct spelling. This could result in the program mixing them up and throwing an error

    def test_display_info(self):
        """
        Tests for the function display info in the script Graph.py

        :return: N/A
        """
        self.assertEqual(g.display_info(g.find_shortest_path("Carboxylic Acid", "")), ['Carboxylic Acid → Alcohol', 'Alcohol → Ketone'])
        # Short Route Info OK - I chose this route as compared to most routes on this graph, it is one of the shorter ones, therefore less information would need to be displayed

        self.assertEqual(g.display_info(g.find_shortest_path("Carboxylic Acid", "Tertiary Alcohol")), ['Carboxylic Acid → Alcohol', 'Alcohol → Halogenoalkane', 'Halogenoalkane → Grignard Reagent', 'Grignard Reagent → Tertiary Alcohol'])
        # Long Route Info OK - I chose this route as compared to most routes on this graph, it is one of the longer ones, therefore more information would need to be displayed so there is a larger probability of an error


# main


if __name__ == "__main__":
    g = ReactionGraph(startNode="Carboxylic Acid", endNode="Ketone")
    unittest.main(verbosity=2)
