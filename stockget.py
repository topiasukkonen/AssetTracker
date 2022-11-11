import yfinance as yf
import sqlite3

class Get1:
    def main(stock):
        #connect to API and local database testi.db
        db = sqlite3.connect("testi.db")
        db.isolation_level = None
        #error handling
        try:
            one = yf.Ticker(stock)
            cg = one.info['regularMarketPrice']
            #get data from API
            lowered = stock.lower()
            print(f"{lowered} is now trading at {cg} USD")
            #insert data into database testi.db
            inserted=(lowered,cg)
            db.execute("INSERT INTO stocks (name, price) VALUES (?, ?)",inserted)
            db.commit()
            #return data for testing purposes
            return f"{lowered} is now trading at {round(cg,0)} USD"
        except:
            #if not available, print error message and return error message for testing purposes
            print("Sorry, that stock is not available.")
            return "Sorry, that stock is not available."
        
        