from ta.momentum import RSIIndicator
from ta.trend import MACD
from ta.volatility import BollingerBands

def generate_indicators(df):
    df['RSI'] = RSIIndicator(close=df['Close']).rsi()
    macd = MACD(close=df['Close'])
    df['MACD'] = macd.macd()
    df['MACD_Signal'] = macd.macd_signal()
    bb = BollingerBands(close=df['Close'])
    df['BB_Upper'] = bb.bollinger_hband()
    df['BB_Lower'] = bb.bollinger_lband()
    df.dropna(inplace=True)
    return df
