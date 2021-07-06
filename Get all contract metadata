import json
import requests
#Returns a list of all contracts on a blockchain along with their metadata.
#Get all contract metadata for AVAX and Ethereum

host = "https://api.covalenthq.com/"
endpoint = 'v1/{chain_id}/tokens/tokenlists/{id}/'
endpoint = endpoint.format(chain_id=43114,id="all")
                           

headers = {
    "cache-control": "public, max-age=10, stale-while-revalidate=30",
    "content-type" : "application/json"
}

parameters = {
    #
    
    "quote-currency" : "USD",
   
    "key":"Your KEY"
    
    
}



request = requests.get(host + endpoint, headers=headers, params=parameters)

json_data = json.loads(request.text)
json_data_str = json.dumps(json_data, indent=2)

print(json_data_str)


#names and AVAX and Ethereum addresses
for transactions in json_data["data"]["items"]:
   
        names=transactions["contract_ticker_symbol"]
        avax=transactions["contract_address"]
        eth=transactions["ethereum_mainnet_address"]                
        print(names,avax, eth)
