# imports
import unittest

from Graph_Display import *


class MyTestCase(unittest.TestCase):
    def test_display_graph(self):
        """
        Tests for the function display_graph in the script Graph_Display.py

        :return: N/A
        """
        self.assertRaises(ValueError, display_graph, False)
        # No Route Between Points - I chose to test this as this would be quite a common occurrence since the user is unable to see the graph and may not remember how to get from one compound to another


if __name__ == "__main__":
    unittest.main(verbosity=2)
