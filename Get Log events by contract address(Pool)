
import json
import requests
#Get transactions

host = "https://api.covalenthq.com/"
endpoint = 'v1/{chain_id}/events/address/{address}/'
endpoint = endpoint.format(chain_id=43114, address="0x1aCf1583bEBdCA21C8025E172D8E8f2817343d65")

#This is ETH-AVAX Pool 0x1aCf1583bEBdCA21C8025E172D8E8f2817343d65

headers = {
    "cache-control": "public, max-age=10, stale-while-revalidate=30",
    "content-type" : "application/json"
    
}

parameters = {
    
    "quote-currency" : "USD",
     "starting-block" : "2292413",
    "ending-block" :"latest",
    "key":"Your KEY"
    
    
}



request = requests.get(host + endpoint, headers=headers, params=parameters)

json_data = json.loads(request.text)
json_data_str = json.dumps(json_data, indent=2)

print(json_data_str)


#We try to take transaction's names and values.

decoded= []
for item in json_data["data"]["items"]:
    decoded.append(item["decoded"])

print(decoded)




#We try to take transaction's names and values.

for transactions in decoded:
        print(transactions["name"])
        
        
#We try to take transaction's names and values.       
        
        

for transactions in decoded:
        names=transactions["name"]
        values=transactions["params"][-1]["value"]
        print(names,values)
        
        
#We try to take transaction's names and values.
        
        
for transactions in decoded:
        names=transactions["name"]
        values=[param["value"] for param in transactions["params"]]
        print(names,values)
        
#We try to take transaction's names and values.        
        
for transactions in decoded:
        names=transactions["name"]
        values=[(param["name"],param["value"]) for param in transactions["params"]]
        print(names,values)
        
#We try to take transaction's names and values.

 for transactions in decoded:
        names=transactions["name"]
        values=[(param["name"],param["value"]) for param in transactions["params"] if param["type"] !="address"]
        print(names,values)
