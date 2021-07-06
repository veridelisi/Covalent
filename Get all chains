import json
import requests
#Get all chains names and labels

host = "https://api.covalenthq.com/"
endpoint = 'v1/chains/'
endpoint = endpoint.format()
                           

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



#We take chains' names and labels
for transactions in json_data["data"]["items"]:
   
        names=transactions["name"]
        label=transactions["label"]
                       
        print(names,label)
        
        
 len(label)
