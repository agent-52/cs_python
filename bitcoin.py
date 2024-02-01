import sys
import requests
import json

if len(sys.argv) != 2:
  sys.exit()

bitcoin = sys.argv[1]
try:
  bitcoin = float(bitcoin)
except ValueError:
  sys.exit("Command-line argument is not a number")
except requests.RequestException:
  sys.exit() 

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

o = response.json()
currency = o["bpi"]
usd = currency["USD"]
rate = usd["rate_float"]
amount = rate*bitcoin

print(f"${amount:,.4f}")

  

    
    


