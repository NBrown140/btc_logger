# btc_logger
Simple python script to log bitcoin price every minute. Used as a cronjob on a Raspberry Pie.

Uses Bitstampy to make API calls to bitstamp and retrieve prices data.

#### Dependencies:
- Bistampy (installed throug pip; https://github.com/unwitting/bitstampy)

#### Setup cron job:

https://crontab.guru/examples.html

http://yellerapp.com/posts/2015-01-12-the-worst-server-setup-you-can-make.html



crontab -e

\* \* \* \* \* python btc_logger.py


