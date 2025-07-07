from nsepython import *

def get_option_chain(symbol="NIFTY"):
    option_data = nse_optionchain_scrapper("nifty", symbol)
    return option_data["records"]["data"]
