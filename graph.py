import sqlite3
import matplotlib.pyplot as plt

class Graph:
    def main(coin):
        #connect to database
        db = sqlite3.connect("testi.db")
        db.isolation_level = None
        #get data from database testi.db
        data=db.execute("SELECT price FROM crypto WHERE name=?",(coin,)).fetchall()
        if data==[]:
            print("Sorry, that chart is not available.")
            return "Sorry, that chart is not available."
        #create a chart of prices using matplotlib, return data for testing purposes
        plt.plot(data)
        plt.show()
        return data