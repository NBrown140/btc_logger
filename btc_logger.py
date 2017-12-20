import bitstamp.client
import csv, os

base_path = r"D:\Bitcoin"

# Get data from bitstamp
public_client = bitstamp.client.Public()

currencies_list = ['btc', 'eur', 'xrp', 'ltc', 'eth', 'bch']

for currency in currencies_list:
	# Log data to file
	row = [public_client.ticker(base=currency, quote="usd")['timestamp'], \
	public_client.ticker(base=currency, quote="usd")['volume'], \
	public_client.ticker(base=currency, quote="usd")['last'], \
	public_client.ticker(base=currency, quote="usd")['high'], \
	public_client.ticker(base=currency, quote="usd")['low'], \
	public_client.ticker(base=currency, quote="usd")['bid'], \
	public_client.ticker(base=currency, quote="usd")['ask']]    
	print row
	path_data = os.path.join(base_path, "bitstamp_"+currency+"_usd.csv")
	with open(path_data, 'ab') as f:
	    w = csv.writer(f)
	    w.writerow(row)

