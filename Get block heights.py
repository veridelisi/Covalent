import json
import requests
#Get block heights
#Retrieve all the block height(s) of a particular chain within a date range. If the end_date is set to latest, return every block height from the start_date to now. 

host = "https://api.covalenthq.com/"
endpoint = 'v1/{chain_id}/block_v2/{start_date}/{end_date}/'
#You need to write start and end date
endpoint = endpoint.format(chain_id=43114, start_date="2021-01-01",end_date="2021-01-30")

headers = {
    "cache-control": "public, max-age=10, stale-while-revalidate=30",
    "content-type" : "application/json"
}

parameters = {
    
    "quote-currency" : "USD",
    #You need to limit (remember every second creating the new one block)
    "limit":"3000",
    "key": "Your KEY"
  
}

request = requests.get(host + endpoint, headers=headers, params=parameters)

json_data = json.loads(request.text)
json_data_str = json.dumps(json_data, indent=2)

print(json_data_str)

#length
len(json_data["data"]["items"])
