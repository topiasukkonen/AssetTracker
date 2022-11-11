import unittest
from stockget import Get1
import yfinance as yf

class TestGet(unittest.TestCase):
    def test_get_coin_available(self):
        one = yf.Ticker("TSLA")
        cg = one.info['regularMarketPrice']
        self.assertEqual(Get1.main("TSLA"), f"b is now trading at {cg} USD")
    
    def test_get_coin_not_available(self):
        self.assertEqual(Get1.main("nostock"), "Sorry, that is not available.")
    