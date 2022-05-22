import requests, json

base_url = r"https://www.alphavantage.co/query?function = CURRENCY_EXCHANGE_RATE"

main_url = base_url + "&from_currency =" + "USD" + "&to_currency =" + "CLP" + "&apikey =" + "VIOJNUBNLIPUAXTH" 
  
    
req_ob = requests.get(main_url)
api = req_ob.json()
print(api)