import requests, json, datetime
from flask_restful import Api, Resource, reqparse, request

class livepeer_staking_alerts(Resource):
	def post(self):

		# URL of livepeer staking alerts by Livepeer.Studio
		url = 'https://livepeer.studio/confirmEmail'
		
		# Decode body params from request
		arguments = ["email", "frequency", "delegatorAddress"]
		parser = reqparse.RequestParser()
		for argument in arguments:
			parser.add_argument(argument)
		args = parser.parse_args()

		# Create payload from body params
		payload = {
			"email": args["email"],
			"frequency": args["frequency"],
			"delegatorAddress": args["delegatorAddress"]
		}

		# Pass headers as application/x-www-form-urlencoded for SendGrid
		headers = {'content-type': 'application/x-www-form-urlencoded',}
		r = requests.post(url, data=payload, headers=headers)
		data = json.loads(r.text)

		# Return data as JSON
		return data