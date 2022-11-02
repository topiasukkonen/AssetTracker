import unittest
from get import Get
from pycoingecko import CoinGeckoAPI

class TestGet(unittest.TestCase):
    def test_get_coin_available(self):
        cg = CoinGeckoAPI()
        data = cg.get_price(ids="bitcoin", vs_currencies='usd')
        self.assertEqual(Get.main("bitcoin"), f"bitcoin is now trading at {data['bitcoin']['usd']} USD")
    
    def test_get_coin_not_available(self):
        self.assertEqual(Get.main("notacoin"), "Sorry, that coin is not available.")
    