import requests, json, datetime
from flask_restful import Api, Resource, reqparse, request

class livepeer_general_info_get_calls(Resource):
	def get(self, service):

		# Check if API service is within acceptable arguments
		if service not in ['all_contract_addresses', 'all_transcoder_campaign_info']:
			return {'data':service + ' is not a function.', 'code':404}

		# Set data var to empty dict
		data = {}

		# Check if service is to get all smart contract addresses
		if service == 'all_contract_addresses':

			# Open the JSON file of all Livepeer smart contracts
			with open('./resources/json_files/livepeer_smart_contracts.json') as json_file:
				
				# Load json file as dict and save as data
				data = json.load(json_file)

		# Check if service is to get all smart contract addresses
		elif service == 'all_transcoder_campaign_info':
			
			# Open the JSON file of all Livepeer Transcoder Campaigns
			with open('./resources/json_files/livepeer_transcoder_campaigns.json') as json_file:

				# Load json file as dict and save as data
				data = json.load(json_file)

		# Return JSON data
		return data