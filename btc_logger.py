from bitstampy import api
import csv, time

path_data = r"D:\Bitcoin\bitcoin_prices.csv"
path_orders = r"D:\Bitcoin\bitcoin_orders.csv"

while True:
	# Get data from bitstamp
	ticker = api.ticker()

	# Log data to file
	row = [ticker['timestamp'], ticker['volume'], ticker['last'], ticker['high'], ticker['low'], ticker['bid'], ticker['ask']]    
	print row
	with open(path_data, 'ab') as f:
	    w = csv.writer(f)
	    w.writerow(row)
	
	# Wait 60 seconds
	#time.sleep(60)
