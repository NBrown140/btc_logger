from datetime import datetime
from shutil import copyfile
from os import remove
import pandas as pd

currentdate = datetime.utcnow().strftime("%Y_%m")

input_data = r"C:\Users\BRONI2\Desktop\bitcoin_prices.csv"
out_raw = r"C:\Users\BRONI2\Desktop\bitcoin_prices_raw_{}.csv".format(currentdate)
out_processed = r"C:\Users\BRONI2\Desktop\bitcoin_prices_processed_{}.csv".format(currentdate)


# Save raw data
copyfile(input_data,out_raw)

# Import csv
df = pd.read_csv(filepath_or_buffer=input_data, sep=',', header=None, 
                 names=['timestamp','volume','last1','high','low','bid','ask'], 
                       index_col='timestamp', parse_dates=True)
# Resmample data to exactly every minute
df_volume_minutely = df.volume.resample('1T').first()
df_last_minutely = df.last1.resample('1T').first()
df_high_minutely = df.high.resample('1T').first()
df_low_minutely = df.low.resample('1T').first()
df_bid_minutely = df.bid.resample('1T').first()
df_ask_minutely = df.ask.resample('1T').first()
# Concatenate back to dataframe
df_out = pd.concat([df_volume_minutely, df_last_minutely, df_high_minutely,
                    df_low_minutely, df_bid_minutely, df_ask_minutely], axis=1)
# Interpolate nans to nearest neighbour
df_out = df_out.interpolate('nearest')


# Save processed data
df_out.to_csv(path_or_buf=out_processed)

# Delete initial data
remove(input_data)
