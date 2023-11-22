import requests
import telegram
import pandas as pd

def get(symbol, interval):
    url = "https://www.binance.com/fapi/v1/continuousKlines?&limit=1000&pair="+ symbol + "&contractType=PERPETUAL&interval=" + interval + ""
    headers = {"User_Agent" : "내 유저 에이전트 아이디"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    value = res.json()
    df = pd.DataFrame(value).astype(float)
    df.columns = ['time', 'open', 'high', 'low', 'close', '5', '6', 'volume', '8', '9', '10', '11']

    return df

def tel_text(text):
    bot = telegram.Bot(token='내 텔레그램 봇 토큰')
    chat_id = 내 텔레그램 챗 아이디
    bot.send_message(chat_id=chat_id, text= text)
