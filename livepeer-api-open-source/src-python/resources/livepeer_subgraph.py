import requests, json, datetime
from flask_restful import Api, Resource, reqparse, request
from resources.coingecko_api import coinGeckoLivepeerCacheAdaptor

coingecko_livepeer_adaptor = coinGeckoLivepeerCacheAdaptor(60)

class livepeer_subgraph_get_calls(Resource):
	def get(self, service):

		if service not in ['get_all_transcoders', 'get_all_rewards', 'get_all_rounds', 'market_data', 'description', 'contract_address', 'tickers']:
			return {'data':service + ' is not a function.', 'code':404}

		args = {}
		json_query = {}
		url = ''

		if service == 'get_all_transcoders':
			query = '{transcoders  {id active ensName status lastRewardRound rewardCut feeShare pricePerSegment pendingRewardCut pendingFeeShare pendingPricePerSegment totalStake}}'
			json_query = {'query': query}
			url = 'https://api.thegraph.com/subgraphs/name/graphprotocol/livepeer'

		if service == 'get_all_rewards':
			query = '{rewards { id round { id initialized length lastInitializedRound startBlock } transcoder { id active ensName status lastRewardRound rewardCut feeShare pricePerSegment pendingRewardCut pendingFeeShare pendingPricePerSegment totalStake} rewardTokens }}'
			json_query = {'query': query}
			url = 'https://api.thegraph.com/subgraphs/name/graphprotocol/livepeer'

		if service == 'get_all_rounds':
			query = '{rounds { id initialized length lastInitializedRound startBlock }}'
			json_query = {'query': query}
			url = 'https://api.thegraph.com/subgraphs/name/graphprotocol/livepeer'

		payload = args
		r = ''
		data = {}
		if service in ['get_all_transcoders', 'get_all_rewards', 'get_all_rounds']:
			r = requests.post(url, json=json_query)
			data = json.loads(r.text)
		else:
			if service in ['market_data', 'description', 'contract_address', 'tickers']:
				data = {service:coingecko_livepeer_adaptor.getLatest()[service]}
				if service == 'market_data':
					data['market_data_in_usd'] = data.pop('market_data')
			else:
				r = requests.get(url, data=payload)
				data = json.loads(r.text)
		return data