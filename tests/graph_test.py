import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    def test_graph_chart_data_shown_appropriately(self):
        #For this particular test to work, you need to have run the program at least once and checked the price of a coin.
        self.assertLess(0, len(Graph.main("bitcoin")))
        
    def test_graph_chart_not_available(self):
        self.assertEqual(Graph.main("notacoin"), "Sorry, that chart is not available.")
    