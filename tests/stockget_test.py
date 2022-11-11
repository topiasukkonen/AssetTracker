import unittest
from stockget import Get1
import yfinance as yf

class TestGet(unittest.TestCase):
    def test_get_stock_available(self):
        one = yf.Ticker("TSLA")
        cg = one.info['regularMarketPrice']
        self.assertEqual(Get1.main("TSLA"), f"tsla is now trading at {round(cg,0)} USD")
    
    def test_get_stock_not_available(self):
        self.assertEqual(Get1.main("nostock"), "Sorry, that stock is not available.")
    