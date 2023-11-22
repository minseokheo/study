import requests
import json
import pandas as pd
import numpy as np

url = "https://fapi.binance.com/fapi/v1/exchangeInfo"

response = requests.get(url)
data = json.loads(response.text)

symbols = data['symbols']

tickers_future = []

for symbol in symbols:
    if symbol['quoteAsset'] == 'USDT':
        tickers_future.append(symbol['symbol'])

for i in tickers_future:
    try:
        url = "https://www.binance.com/api/v3/uiKlines?limit=1000&symbol=" + i + "&interval=5m"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
        res = requests.get(url, headers=headers)
        res.raise_for_status()

        value = res.json()
        df = pd.DataFrame(value)
        df.columns = ['time', 'open', 'high', 'low', 'close', 'volume', '6', 'volume_asset', '8', '9', '10', '11']

        volume = df['volume_asset'].astype(float)
        close = df['close'].astype(float)

        close998 = close.iloc[-2]
        close997 = close.iloc[-3]
        volume998 = volume.iloc[-2]

        volume_range = volume[0:997]
        volume_avg = np.average(volume_range)
        volume_ratio = round(volume998 / volume_avg, 1)

        print(i + "  " + str(volume_ratio) + "배")

    except Exception as e:
        if str(e).startswith('429'):
            print("Too many requests")
        else:
            pass