import requests
import json

while True:
  response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

  o = response.json()
  currency = o["bpi"]
  usd = currency["USD"]
  rate = usd["rate_float"]
  amount = rate*1

  print(f"${amount:,.4f}")