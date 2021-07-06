import json
import requests
#Get historical portfolio value over time 
#Given chain_id and wallet address, return wallet value for the last 30 days at 24 hour timestamps. 

host = "https://api.covalenthq.com/"
endpoint = 'v1/{chain_id}/address/{address}/portfolio_v2/'
endpoint = endpoint.format(chain_id=43114, address="0x30dfdc78173766ba26127afd1aaaad6e183d8762")

headers = {
    "cache-control": "public, max-age=10, stale-while-revalidate=30",
    "content-type" : "application/json"
}

parameters = {
    
    "quote-currency" : "USD",
    "key": "Your KEY"
  
}

request = requests.get(host + endpoint, headers=headers, params=parameters)

json_data = json.loads(request.text)
json_data_str = json.dumps(json_data, indent=2)

print(json_data_str)


#The contract names which I made transactions
contract_names = []

for item in json_data["items"]:
    contract_names.append(item["contract_name"])

contract_names

#The sub details

holdings = []

for item in json_data["items"]:
    holdings.append(item["holdings"])

holdings 

#The 6 coin's details

len(holdings)


#The first coin's quote rates

quote_rate = []

for item in holdings[0]:
    quote_rate.append(item["quote_rate"])

quote_rate

#The second coin's quote rates

quote_rate1 = []

for item in holdings[1]:
    quote_rate1.append(item["quote_rate"])

quote_rate1

#The all coin's quote rates

for item in json_data["items"]:
    for holding in item["holdings"]:
        if holding["quote_rate"] is not None:
            print(item["contract_ticker_symbol"],holding["timestamp"],holding["quote_rate"])
