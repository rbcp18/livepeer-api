import requests, json, datetime

class coinGeckoLivepeerCacheAdaptor(object):
	def __init__(self, refreshPeriodInSeconds):
	    self.refreshPeriodInSeconds = refreshPeriodInSeconds
	    self.data = None
	    self.lastRefresh = datetime.datetime(1970,1,1)

	def _refreshData(self):
		url = 'https://api.coingecko.com/api/v3/coins/livepeer'
		r = requests.get(url)
		data = json.loads(r.text)
		
		service = 'market_data'
		del data[service]['roi']
		del data[service]['market_cap']
		del data[service]['market_cap_rank']
		del data[service]['market_cap_change_24h_in_currency']
		del data[service]['market_cap_change_percentage_24h_in_currency']
		del data[service]['total_supply']
		del data[service]['circulating_supply']
		data[service]['current_price'] = data[service]['current_price']['usd']
		data[service]['ath'] = data[service]['ath']['usd']
		data[service]['ath_change_percentage'] = data[service]['ath_change_percentage']['usd']
		data[service]['ath_date'] = data[service]['ath_date']['usd']
		data[service]['total_volume'] = data[service]['total_volume']['usd']
		data[service]['high_24h'] = data[service]['high_24h']['usd']
		data[service]['low_24h'] = data[service]['low_24h']['usd']
		data[service]['price_change_24h_in_currency'] = data[service]['price_change_24h_in_currency']['usd']
		data[service]['price_change_percentage_1h_in_currency'] = data[service]['price_change_percentage_1h_in_currency']['usd']
		data[service]['price_change_percentage_24h_in_currency'] = data[service]['price_change_percentage_24h_in_currency']['usd']
		data[service]['price_change_percentage_7d_in_currency'] = data[service]['price_change_percentage_7d_in_currency']['usd']
		data[service]['price_change_percentage_14d_in_currency'] = data[service]['price_change_percentage_14d_in_currency']['usd']
		data[service]['price_change_percentage_30d_in_currency'] = data[service]['price_change_percentage_30d_in_currency']['usd']
		data[service]['price_change_percentage_60d_in_currency'] = data[service]['price_change_percentage_60d_in_currency']['usd']
		data[service]['price_change_percentage_200d_in_currency'] = data[service]['price_change_percentage_200d_in_currency']['usd']

		self.data = data
		self.lastRefresh = datetime.datetime.now()

	def getLatest(self):
	    if (self.lastRefresh + datetime.timedelta(seconds = self.refreshPeriodInSeconds)) < datetime.datetime.now():
	        self._refreshData()
	    return self.data