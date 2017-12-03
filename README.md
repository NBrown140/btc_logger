# btc_logger
Simple python script to log bitcoin price every minute. Used as a cronjob on a Raspberry Pie.

Uses bitstamp-python-client to make API calls to bitstamp and retrieve prices data.

monthly_cleaner.py should be called at the very end of each month to process data.

### Dependencies:
- bitstamp-python-client (installed throug pip; https://github.com/kmadac/bitstamp-python-client)

### Setup cron job:

https://crontab.guru/examples.html

http://yellerapp.com/posts/2015-01-12-the-worst-server-setup-you-can-make.html


#### Daily cron job
crontab -e

\* \* \* \* \* python btc_logger.py


#### Monthly cron job
crontab -e

0 0 1 \* \* python monthly_cleaner.py
