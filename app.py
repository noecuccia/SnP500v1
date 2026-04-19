import yfinance as yf

sp500 = yf.Ticker("^GSPC")
prix = sp500.info["regularMarketPrice"]
print(prix)
