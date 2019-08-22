import requests, json, datetime
from flask_restful import Api, Resource, reqparse, request

# Get current ETH block height (in decimal)
def getCurrentEthereumBlock():
   try:
       # Pings Etherscan for the current block
       resp = requests.get('https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken')
       
       # Convert block number to integer
       block = int(resp.json()['result'], 16)

       return block
   except:
       return -1

# Get all transactions for a single address in a block range
def getTxnsForBlockRange(address, startBlock, endBlock):
   try:
       # Pings Ethererscan for transactions by address
       url = 'http://api.etherscan.io/api?module=account&action=txlist&address={}&startblock={}&endblock={}&sort=desc&apikey=YourApiKeyToken'
       
       resp = requests.get(url.format(address, startBlock, endBlock))
       
       txns = resp.json()['result']
       return txns
   except:
       return None

# Return all the transactions given multiple addresses
def getTxnsInLastNDays(addresses, days):
   # Get current block number
   curBlock = getCurrentEthereumBlock()
   
   # Get starting block number
   startBlock = curBlock - int(days * 4 * 60 * 24)
   allTxns = []
   for address in addresses:
       
       result = getTxnsForBlockRange(address, startBlock, curBlock)
       
       if result is not None:
           
           # Add transactions to allTxns
           allTxns.extend(result)
   return allTxns

class livepeer_lpt_transactions(Resource):
	def get(self, service):

		if service not in ['get_all_lpt_transactions_from_multiple_wallets']:
			return {'data':service + ' is not a function.', 'code':404}

		def parse_params(arguments):
			# API call params parser.
			parser = reqparse.RequestParser()
			for argument in arguments:
				parser.add_argument(argument)
			return parser

		# Declare data variable.
		data = {}
		
		if service == "get_all_lpt_transactions_from_multiple_wallets":

			# Decode body params from request
			arguments = ["addresses", "days"]
			parser = parse_params(arguments)
			
			args = parser.parse_args()

			# Declare query params as variables
			addresses = args["addresses"]
			days = args["days"]
			
			# Replace "%2C" with ",". This switch of "," for "%2C" can occur when API is queried.
			wallet_addresses = addresses.replace('%2C',',')

			# Retrieve the transactions for multiple wallets over the stated number of days.
			data = getTxnsInLastNDays([wallet_addresses], float(days))

		# Return data as JSON
		return data

