import yfinance as yf
import joblib
from backend.indicators import generate_indicators
from backend.fetch_data import get_option_chain
from backend.option_screener import filter_profitable_options

def run_prediction():
    model = joblib.load("model/nifty_model.pkl")
    df = yf.download("^NSEI", period="15d", interval="5m")
    df = generate_indicators(df)

    latest = df[['RSI', 'MACD', 'MACD_Signal', 'BB_Upper', 'BB_Lower']].iloc[-1:]
    direction = model.predict(latest)[0]
    spot_price = df['Close'].iloc[-1]

    options = get_option_chain()
    suggestions = filter_profitable_options(options, direction, spot_price)

    return direction, spot_price, suggestions
