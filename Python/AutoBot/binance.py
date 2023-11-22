import requests
import telegram
import pandas as pd

def get(symbol, interval):
    url = "https://www.binance.com/fapi/v1/continuousKlines?&limit=1000&pair="+ symbol + "&contractType=PERPETUAL&interval=" + interval + ""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    value = res.json()
    df = pd.DataFrame(value).astype(float)
    df.columns = ['time', 'open', 'high', 'low', 'close', '5', '6', 'volume', '8', '9', '10', '11']

    return df

def tel_text(text):
    bot = telegram.Bot(token='6933439156:AAF9B_X1HGwNUjkKtp1JnA974HXc5ak00WI')
    chat_id = 6730388900
    bot.send_message(chat_id=chat_id, text= text)