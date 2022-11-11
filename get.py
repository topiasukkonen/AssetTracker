from pycoingecko import CoinGeckoAPI
import sqlite3

class Get:
    def main(coi):
        #connect to CoinGecko API and local database testi.db
        cg = CoinGeckoAPI()
        db = sqlite3.connect("testi.db")
        db.isolation_level = None
        #error handling for coins that are not available on CoinGecko API
        try:
            #get data from CoinGecko API
            data = cg.get_price(ids=coi, vs_currencies='usd')
            print(f"{coi} is now trading at {data[coi]['usd']} USD")
            #insert data into database testi.db
            price=float(data[coi]['usd'])
            name=coi
            inserted=(name,price)
            db.execute("INSERT INTO crypto (name, price) VALUES (?, ?)",inserted)
            db.commit()
            #return data for testing purposes
            #return f"{coi} is now trading at {data[coi]['usd']} USD"
            return coi
        except:
            #if coin is not available, print error message and return error message for testing purposes
            print("Sorry, that coin is not available.")
            return "Sorry, that coin is not available."