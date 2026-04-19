import yfinance as yf
from datetime import datetime

def get_snp500_live():
    ticker = yf.Ticker("^GSPC")
    info = ticker.info

    prix = info.get("regularMarketPrice")
    ouverture = info.get("regularMarketOpen")
    variation = prix - ouverture if prix and ouverture else None
    variation_pct = (variation / ouverture * 100) if variation else None
    volume = info.get("regularMarketVolume")
    haut = info.get("regularMarketDayHigh")
    bas = info.get("regularMarketDayLow")

    print(f"=== S&P 500 - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} ===")
    print(f"Prix actuel : {prix:.2f} $")
    print(f"Variation   : {variation:+.2f} $ ({variation_pct:+.2f}%)")
    print(f"Haut / Bas  : {haut:.2f} $ / {bas:.2f} $")
    print(f"Volume      : {volume:,}")

if __name__ == "__main__":
    get_snp500_live()
