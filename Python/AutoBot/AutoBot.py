
import binance as bn
import threading


def rsi(symbol, interval, period):
    try:
        close = bn.get(symbol, interval)['close']
        delta = close.diff(1)
        # close 행과 행의 차이를 구합니다. 간격은 1입니다.
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        # gain(상승폭)은 delta가 양수면 delta를 그대로 들여오고 나머지는 0으로 반환합니다.
        # loss의 경우 반대로 하되 음수가 되므로 앞에 마이너스 부호를 붙여줍니다.

        c = period - 1
        a = 1 / period

        # 지수가중이동평균을 구하기 위해 필요한 계수입니다. 둘 중 하나만 사용하시면 됩니다.
        # com = c , alpha = a

        AU = gain.ewm(alpha=(a)).mean()
        AD = loss.ewm(alpha=(a)).mean()
        # ewm().mean()는 지수가중이동평균을 구하는 함수입니다. 매개변수로 a값을 넣어줍니다.
        RS = AU / AD

        RSI = round((RS / (1 + RS)) * 100, 2)
        return RSI


    except Exception as e:
        if str(e).startswith('429'):
            bn.tel_text(symbol + "  " + str(e))
    else:
        pass


tickers = ['KLAYUSDT', 'SEIUSDT', 'GASUSDT', 'QNTUSDT', 'UMAUSDT', 'QTUMUSDT', 'OPUSDT', 'TUSDT', 'RVNUSDT', 'FXSUSDT', 'CELRUSDT', 'RNDRUSDT', 'DGBUSDT', 'ETCUSDT', '1INCHUSDT', 'ANTUSDT', 'STGUSDT', 'FETUSDT', 'ACHUSDT', '1000FLOKIUSDT', 'AGLDUSDT', 'CHZUSDT', 'ORDIUSDT', 'MEMEUSDT', 'YGGUSDT', 'MBLUSDT', 'AUDIOUSDT', 'WAVESUSDT', 'CRVUSDT', 'ARBUSDT', 'JOEUSDT', 'IOTAUSDT', 'PEOPLEUSDT', 'GMXUSDT', 'MAGICUSDT', 'WAXPUSDT', 'SUSHIUSDT', 'BATUSDT', 'FOOTBALLUSDT', 'XEMUSDT', 'ANKRUSDT', 'TLMUSDT', 'IOSTUSDT', 'COMPUSDT', 'THETAUSDT', 'HOTUSDT', 'BTCDOMUSDT', 'OCEANUSDT', 'LITUSDT', 'ALICEUSDT', 'POLYXUSDT', 'AAVEUSDT', 'CVXUSDT', 'BADGERUSDT', 'ARPAUSDT', 'MINAUSDT', 'DOTUSDT', 'ARUSDT', 'ICXUSDT', 'MKRUSDT', 'RLCUSDT', '1000BONKUSDT', 'DASHUSDT', 'GMTUSDT', 'IDEXUSDT', 'ZENUSDT', 'LTCUSDT', 'LDOUSDT', 'CAKEUSDT', 'OXTUSDT', 'BONDUSDT', 'TIAUSDT', 'TRBUSDT', 'ALGOUSDT', 'IMXUSDT', 'BLUEBIRDUSDT', 'ARKMUSDT', 'EGLDUSDT', 'BNTUSDT', 'ENJUSDT', 'JASMYUSDT', 'KNCUSDT', 'KEYUSDT', 'DUSKUSDT', 'EDUUSDT', 'GRTUSDT', 'HIFIUSDT', 'ORBSUSDT', 'ATAUSDT', 'STORJUSDT', 'ONTUSDT', 'GALUSDT', 'FTMUSDT', 'RUNEUSDT', 'XLMUSDT', 'BLZUSDT', 'NKNUSDT', 'STXUSDT', 'IDUSDT', 'XMRUSDT', 'SFPUSDT', 'PENDLEUSDT', 'LINAUSDT', 'FRONTUSDT', 'CHRUSDT', 'BSVUSDT', 'DOGEUSDT', 'LQTYUSDT', 'KSMUSDT', 'BTCUSDT', 'SNXUSDT', 'ARKUSDT', 'CELOUSDT', 'ICPUSDT', 'APTUSDT', 'DARUSDT', 'BTCSTUSDT', 'PHBUSDT', 'SUIUSDT', 'SSVUSDT', 'MATICUSDT', 'GTCUSDT', 'DENTUSDT', 'SPELLUSDT', 'ETHUSDT_240329', 'TWTUSDT', 'VETUSDT', 'SOLUSDT', 'CFXUSDT', 'HFTUSDT', 'REEFUSDT', 'XRPUSDT', 'API3USDT', 'BANDUSDT', 'ONEUSDT', '1000SHIBUSDT', 'CKBUSDT', 'ILVUSDT', 'ENSUSDT', 'AGIXUSDT', 'IOTXUSDT', 'ZRXUSDT', 'HBARUSDT', '1000XECUSDT', 'BLURUSDT', 'BEAMXUSDT', 'TOMOUSDT', 'KAVAUSDT', 'USDCUSDT', 'GLMRUSDT', 'STRAXUSDT', 'DODOXUSDT', 'FLMUSDT', 'CTSIUSDT', 'RDNTUSDT', 'XVGUSDT', 'OMGUSDT', 'YFIUSDT', 'DYDXUSDT', 'ROSEUSDT', 'LINKUSDT', 'PERPUSDT', 'NMRUSDT', 'CYBERUSDT', 'C98USDT', 'MAVUSDT', 'ETHUSDT', 'WOOUSDT', 'LPTUSDT', 'STEEMUSDT', 'AMBUSDT', 'RIFUSDT', 'NEARUSDT', 'ALPHAUSDT', 'ETHUSDT_231229', 'WLDUSDT', 'XVSUSDT', 'APEUSDT', 'SNTUSDT', 'DEFIUSDT', '1000PEPEUSDT', 'UNIUSDT', 'BNBUSDT', 'POWRUSDT', 'BALUSDT', 'BNXUSDT', 'FILUSDT', 'HOOKUSDT', 'LRCUSDT', 'SANDUSDT', 'PYTHUSDT', 'RSRUSDT', 'ATOMUSDT', 'MANAUSDT', 'ASTRUSDT', 'RENUSDT', 'HIGHUSDT', 'SLPUSDT', 'TOKENUSDT', 'NTRNUSDT', 'AVAXUSDT', 'OGNUSDT', 'BTCUSDT_240329', 'STPTUSDT', 'BCHUSDT', '1000LUNCUSDT', 'LOOMUSDT', 'EOSUSDT', 'MASKUSDT', 'TRUUSDT', 'XTZUSDT', 'NEOUSDT', 'LUNA2USDT', 'MTLUSDT', 'LEVERUSDT', 'BTCUSDT_231229', 'TRXUSDT', 'UNFIUSDT', 'INJUSDT', 'COMBOUSDT', 'ADAUSDT', 'ZILUSDT', 'BAKEUSDT', 'AXSUSDT', 'RADUSDT', 'GALAUSDT', 'ZECUSDT', 'FLOWUSDT', 'MDTUSDT', 'BELUSDT', 'COTIUSDT', 'STMXUSDT', 'CTKUSDT', 'BIGTIMEUSDT', 'BICOUSDT', 'SKLUSDT', 'KASUSDT', 'SXPUSDT']

def run():
    for i in tickers:
        try:
            RSI = rsi(i, "5m", 14)
            RSI998 = RSI.iloc[-2]
            if RSI998 <= 20:
                bn.tel_text(i + "  RSI: " + str(RSI998))
            elif RSI998 >= 80:
                bn.tel_text(i + "  RSI: " + str(RSI998))
        except AttributeError as ae:
            # 예외 처리 추가
            print(f"AttributeError: {ae}")

    threading.Timer(270, run).start()

run()
