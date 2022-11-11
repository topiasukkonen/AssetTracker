import unittest
from stockgraph import Graph1

class TestGraph(unittest.TestCase):
    def test_graph_chart_data_shown_appropriately(self):
        #For this particular test to work, you need to  run the program at least once and check the price of a stock.
        self.assertLess(0, len(Graph1.main("TSLA")))
        
    def test_graph_chart_not_available(self):
        self.assertEqual(Graph1.main("eiei"), "Sorry, that chart is not available.")
    