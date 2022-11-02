from get import Get
from graph import Graph
#terminal text interface for the program
print("Welcome to Cryptotracker!")
while True:
    choose=input("What would you like to do? Type 'get' to see current prices, 'graph' to see a graph of the prices of a particular coin you have checked the price of, or 'exit' to exit the program: ")
    if choose=="get":
        coi=input("What coin would you like to see the price of as USD? ")
        Get.main(coi)
    elif choose=="graph":
        coin=input("What coin would you like to see the graph of? ")
        Graph.main(coin)
    elif choose=="exit":
        print("Thank you for using Cryptotracker! Hope to see you again soon!")
        break