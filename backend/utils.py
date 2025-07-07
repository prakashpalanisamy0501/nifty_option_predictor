import datetime

def get_nearest_thursday():
    """Return the nearest Thursday expiry date."""
    today = datetime.date.today()
    days_ahead = 3 - today.weekday()  # 3 = Thursday
    if days_ahead <= 0:
        days_ahead += 7
    expiry = today + datetime.timedelta(days=days_ahead)
    return expiry.strftime("%d-%b-%Y")

def round_to_nearest_50(x):
    return int(round(x / 50.0)) * 50

def is_market_open():
    now = datetime.datetime.now().time()
    market_start = datetime.time(9, 15)
    market_end = datetime.time(15, 30)
    return market_start <= now <= market_end
