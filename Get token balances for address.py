import json
import requests
#Get token balances for address 
#Return a list of all ERC20 and NFT token balances along with their current spot prices. 

host = "https://api.covalenthq.com/"
endpoint = 'v1/{chain_id}/address/{address}/balances_v2/'
endpoint = endpoint.format(chain_id=43114, address="0x30dfdc78173766ba26127afd1aaaad6e183d8762")

#My address is 0x30dfdc78173766ba26127afd1aaaad6e183d8762

headers = {
    "cache-control": "public, max-age=10, stale-while-revalidate=30",
    "content-type" : "application/json"
}

parameters = {
  
    "quote-currency" : "USD",
    "key": "YOUR API PLEASE"
}

request = requests.get(host + endpoint, headers=headers, params=parameters)

json_data = json.loads(request.text)
json_data_str = json.dumps(json_data, indent=2)

print(json_data_str)

#I had transactions with only 6 contracts
len(json_data["data"]["items"])



#My transactions' names

contract_names = []

for item in json_data["data"]["items"]:
    contract_names.append(item["contract_name"])

contract_names



#My transactions' amounts
amount = []

for item in json_data["data"]["items"]:
    amount.append(item["balance"])

amount


#install
pip install pandas
pip install numpy


#WE convert our lists to the Dataframe
import pandas as pd
df = pd.DataFrame(list(zip(contract_names, amount)),columns=['names', 'amounts'])
df

#WE converts 18 digits to normal numbers
df["amounts2"] = df["amounts"].astype('float') / pow(10,18)
df["amounts2"].astype('float')
df["amounts2"]

#WE converts 18 digits to normal numbers
df["amounts2"]=df["amounts2"].apply(lambda x : "{0:.6f}".format(x))

#Last dataframe
df2=df[['names','amounts2']]  
df2



