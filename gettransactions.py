import json
import requests
#Get a transaction. Retrieve a single transaction for tx_hash including their decoded log events.

host = "https://api.covalenthq.com/"
endpoint = 'v1/{chain_id}/transaction_v2/{tx_hash}/'
endpoint = endpoint.format(chain_id=43114,tx_hash="0x8dee4a9c83faf0f86170a6211ec8160a307dfd1ece88e5a39378b912ef862374")
                           
#My transaction 0x8dee4a9c83faf0f86170a6211ec8160a307dfd1ece88e5a39378b912ef862374
#https://cchain.explorer.avax.network/tx/0x8dee4a9c83faf0f86170a6211ec8160a307dfd1ece88e5a39378b912ef862374/token-transfers

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

#Events and amounts
for transactions in json_data["data"]["items"]:
    for item in transactions["log_events"]:
        names=item["decoded"]["name"]
        values=item["decoded"]["params"][-1]["value"]
        print(names,values)
        

