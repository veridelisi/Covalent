import json
import requests
#Get Log events by contract address 

host = "https://api.covalenthq.com/"
endpoint = 'v1/{chain_id}/events/address/{address}/'
endpoint = endpoint.format(chain_id=43114, address="0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7")

#WAVAX contract address is 0xB31f66AA3C1e785363F0875A1B74E27b85FD66c7

headers = {
    "cache-control": "public, max-age=10, stale-while-revalidate=30",
    "content-type" : "application/json"
}

parameters = {
    #Blocks numbers'
    "starting-block": "2249592",
    "ending-block": "latest",
    "quote-currency" : "USD",
    
    "key":"Your KEY"
    
    
}



request = requests.get(host + endpoint, headers=headers, params=parameters)

json_data = json.loads(request.text)
json_data_str = json.dumps(json_data, indent=2)

print(json_data_str)



#We take transactions' names and values

for transactions in json_data["data"]["items"]:
   
        names=transactions["decoded"]["name"]
        values=transactions["decoded"]["params"][-1]["value"]
        print(names,values)
        
        

#We take transactions' names and values        
        
        
        
 for transactions in json_data["data"]["items"]:
   
        names=transactions["decoded"]["name"]
        values=[param["value"] for param in transactions["decoded"]["params"]]
        print(names,values)
        
        
 
#We take transactions' names and values       
        
  for transactions in json_data["data"]["items"]:
   
        names=transactions["decoded"]["name"]
        values=[(param["name"],param["value"]) for param in transactions["decoded"]["params"]]
        print(names,values)
        
        
  
#We take transactions' names and values      
        
   for transactions in json_data["data"]["items"]:
  
        names=transactions["decoded"]["name"]
        values=[(param["name"],param["value"]) for param in transactions["decoded"]["params"] if param["type"] !="address"]
        print(names,values)
        
        
        
        
  
