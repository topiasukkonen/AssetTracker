from pycoingecko import CoinGeckoAPI
import sqlite3

class Get:
    def main(coi):
        cg = CoinGeckoAPI()
        db = sqlite3.connect("testi.db")
        db.isolation_level = None
        try:
            data = cg.get_price(ids=coi, vs_currencies='usd')
            print(f"{coi} is now trading at {data[coi]['usd']} USD")
            price=float(data[coi]['usd'])
            name=coi
            inserted=(name,price)
            db.execute("INSERT INTO crypto (name, price) VALUES (?, ?)",inserted)
            db.commit()
            return f"{coi} is now trading at {data[coi]['usd']} USD"
        except:
            print("Sorry, that coin is not available.")
            return "Sorry, that coin is not available."