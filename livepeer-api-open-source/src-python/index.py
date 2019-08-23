from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_sslify import SSLify
from resources.livepeer_subgraph import livepeer_subgraph_get_calls
from resources.livepeer_staking_alerts import livepeer_staking_alerts
from resources.livepeer_general_info import livepeer_general_info_get_calls
from resources.livepeer_lpt_transactions import livepeer_lpt_transactions
from resources.livepeer_exchange_data import livepeer_exchange_data

app = Flask(__name__)
app.config['RESTFUL_JSON'] = {'indent':None, 'separators':(',',':')}
sslify = SSLify(app)
api = Api(app) 

api.add_resource(livepeer_subgraph_get_calls, "/livepeer/<string:service>")
api.add_resource(livepeer_staking_alerts, "/livepeer/staking-alerts/confirmEmail")
api.add_resource(livepeer_general_info_get_calls, "/livepeer/info/<string:service>")
api.add_resource(livepeer_lpt_transactions, "/livepeer/transactions/<string:service>")
api.add_resource(livepeer_exchange_data, "/livepeer/exchanges/<string:service>")

#Development
app.run(debug=True)

#Production
#if __name__ == "__main__":
#    application.run(host='0.0.0.0')