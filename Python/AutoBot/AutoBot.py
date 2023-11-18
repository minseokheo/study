import requests
import pandas as pd

url = "https://www.binance.com/fapi/v1/continuousKlines?endTime=1700646322000&limit=1000&pair=BNBUSDT&contractType=PERPETUAL&interval=5m"
headers = {"User-Agent" :
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

value = res.json()
df = pd.DataFrame(value)

print(df)