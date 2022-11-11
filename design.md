# Visual representation of the product design

![bitmap](https://user-images.githubusercontent.com/96625505/199540892-e645adb7-9152-40a3-9a1a-047e70012816.png)

- The image above shows the design of previous version, Cryptotracker. However, the design of AssetTracker is basically the same: only one additional API is used via service stockget.py and an additional stockgraph.py handles the database connection for stock data. 
- User has access to the data provided through index.py, which connects to either get.py, graph.py, stockget.py, stockgraph.py
- Get files fetch real time data, so they connect to the API and then returns price of the asset in question
- Graph files use local testi.db (or other similar) file to form a chart from the price points it has saved when user has fetched data from the API

Data is stored permanently to the database file, so it can be used even after the program is shut down.

Error handling is done quite minimalistically by try-except -clauses. Could be improved in the future (in hand with many other things), though does the job fairly well at present.