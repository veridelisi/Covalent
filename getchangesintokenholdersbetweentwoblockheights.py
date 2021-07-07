import json
import requests
#Get changes in token holders between two block heights

host = "https://api.covalenthq.com/"
endpoint = 'v1/{chain_id}/tokens/{address}/token_holders_changes/'
endpoint = endpoint.format(chain_id=43114, address="0x60781C2586D68229fde47564546784ab3fACA982")
                           
#This is PNG Contract Details

headers = {
    "cache-control": "public, max-age=10, stale-while-revalidate=30",
    "content-type" : "application/json"
}

parameters = {
    #Blocks numbers'
    "starting-block": "1974368",
    "ending-block": "1974369",
    "quote-currency" : "USD",
   
    "key":"Your KEY"
    
    
}



request = requests.get(host + endpoint, headers=headers, params=parameters)

json_data = json.loads(request.text)
json_data_str = json.dumps(json_data, indent=2)

print(json_data_str)



#Token holders and their wealth change.
for transactions in json_data["data"]["items"]:
   
        names=transactions["token_holder"]
        values=transactions["diff"]
        print(names,values)
