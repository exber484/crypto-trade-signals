from flask import Flask, jsonify
import requests
import numpy as np
import talib

app = Flask(__name__)

# CoinMarketCap API anahtarınız buraya (yerine kendi anahtarınızı ekleyin)
API_KEY = "YOUR_COINMARKETCAP_API_KEY"

# CoinMarketCap API'sinden ilk 500 kripto para verilerini alma
def get_crypto_data():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": API_KEY,
    }
    params = {"limit": 500, "convert": "USD"}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data["data"]

# Teknik analiz sinyalleri üretme
def generate_signals(data):
    signals = []
    for coin in data:
        prices = np.random.random(500)  # Örnek fiyat verisi simülasyonu
        rsi = talib.RSI(prices, timeperiod=14)
        macd, macdsignal, macdhist = talib.MACD(prices, fastperiod=12, slowperiod=26, signalperiod=9)
        sma_short = talib.SMA(prices, timeperiod=20)
        sma_long = talib.SMA(prices, timeperiod=50)

        # Sinyaller
        signal = {
            "coin": coin["name"],
            "rsi": "buy" if rsi[-1] < 30 else "sell" if rsi[-1] > 70 else "hold",
            "macd": "buy" if macd[-1] > macdsignal[-1] else "sell",
            "trend": "buy" if sma_short[-1] > sma_long[-1] else "sell",
        }
        signals.append(signal)
    return signals

@app.route('/')
def home():
    return "Kripto Para Alım-Satım Sinyalleri API'sine Hoş Geldiniz!"

@app.route('/api/signal')
def signal():
    data = get_crypto_data()
    signals = generate_signals(data)
    return jsonify(signals)

if __name__ == '__main__':
    app.run(debug=True)
