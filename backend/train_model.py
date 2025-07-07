import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import MACD
from ta.volatility import BollingerBands
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import joblib
import os

# Download NIFTY data
df = yf.download("^NSEI", start="2020-01-01", interval="1d")
df['RSI'] = RSIIndicator(close=df['Close']).rsi()
macd = MACD(close=df['Close'])
df['MACD'] = macd.macd()
df['MACD_Signal'] = macd.macd_signal()
bb = BollingerBands(close=df['Close'])
df['BB_Upper'] = bb.bollinger_hband()
df['BB_Lower'] = bb.bollinger_lband()
df.dropna(inplace=True)

# Label: 1 if next day is up, else 0
df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)

features = ['RSI', 'MACD', 'MACD_Signal', 'BB_Upper', 'BB_Lower']
X = df[features]
y = df['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)

model = XGBClassifier()
model.fit(X_train, y_train)

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/nifty_model.pkl")

print("✅ Model trained and saved to model/nifty_model.pkl")
