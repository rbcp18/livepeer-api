import requests, json, datetime
from flask_restful import Api, Resource, reqparse, request

class livepeer_exchange_data(Resource):
	def get(self, service):

		# Declar data variable
		data = {}

		if 'radar-relay-' in service:

			#services include radar-relay-ticker, radar-relay-stats, radar-relay-history, radar-relay-fills, radar-relay-candles, radar-relay-book

			# URL of Radar Relay API for LPT market
			url = "https://api.radarrelay.com/v2/markets/lpt-weth/" + service.replace('radar-relay-','')
			
			# Run GET request on Radar Relay data
			r = requests.get(url)

			# Convert data to JSON
			data = json.loads(r.text)

		if 'poloniex-' in service:

			#services include poloniex-returnTradeHistory, poloniex-return24hVolume, poloniex-returnOrderBook

			# URL of Poloniex API for LPT market
			url = "https://poloniex.com/public?command="+service.replace('poloniex-','')+"&currencyPair=BTC_LPT"

			# Run GET request on Poloniex data
			r = requests.get(url)

			# Convert data to JSON
			data = json.loads(r.text)

		if 'idex-' in service:

			#services include idex-returnTradeHistory, idex-returnOrderBook

			# URL of Poloniex API for LPT market
			url = "https://api.idex.market/"+service.replace('idex-','')

			# Payload to include for LPT market
			payload = {
				"market": "ETH_LPT"
			}

			# Run GET request on IDEX data
			r = requests.post(url, data=payload)

			# Convert data to JSON
			data = json.loads(r.text)

		# Return data as JSON
		return data