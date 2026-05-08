import yfinance as yf

# get(sym) returns the information related to a symbol from yfinance
def fetch(sym:str):
    try:
        # pull ticker  information from symbol
        ticker = yf.Ticker(sym)
        info = ticker.info

        # return none if no information is available
        if not info or "symbol" not in info:
            return None

        # return the ticker
        return ticker

    except Exception:
        return None