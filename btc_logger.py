from bitstampy import api
import csv

path_data = r"D:\Bitcoin\bitcoin_prices.csv"

# Get data from bitstamp
ticker = api.ticker()

# Log data to file
row = [ticker['timestamp'], ticker['volume'], ticker['last'], ticker['high'], ticker['low'], ticker['bid'], ticker['ask']]    
print row
with open(path_data, 'ab') as f:
    w = csv.writer(f)
    w.writerow(row)

