# AssetTracker

AssetTracker is a Python program that fetches crypto and stock data from two APIs, stores it to local database using SQLite and visualizes it using Matplotlib.

# How to use?
 
 Download the latest release:
 
https://github.com/topiasukkonen/AssetTracker/releases/tag/assettracker
 
 Project is tested locally using Python 3.10.6, so this version is recommended.
 
 Install SQLite3 using pip as follows
 
 ```
 pip install sqlite3
```
 
 
 Install other dependencies listed in requirements.txt file using pip the way shown above.
 
 Finally, go to the root of the project and run the program as follows
 
 ```
 python3 index.py
```

Insert crypto names or stock names as stock tickers to the input fields provided and press the corresponding button. Current prices will be shown in the terminal while historical price data is shown as a chart in a separate pop up window.

Check also:

https://github.com/topiasukkonen/AssetTracker/blob/main/tests.md

https://github.com/topiasukkonen/AssetTracker/blob/main/hours.md

https://github.com/topiasukkonen/AssetTracker/blob/main/design.md
