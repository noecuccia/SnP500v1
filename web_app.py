import yfinance as yf
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    sp500 = yf.Ticker("^GSPC")
    prix = sp500.info["regularMarketPrice"]
    return f"Prix du S&P 500 : {prix}"

if __name__ == "__main__":
    app.run(debug=True)

