import yfinance as yf

# 미국(애플) 및 한국(삼성전자) 주식 데이터 가져오기
stocks = {"AAPL": "애플", "005930.KS": "삼성전자"}

for ticker_symbol, name in stocks.items():
    ticker = yf.Ticker(ticker_symbol)
    try:
        stock_info = ticker.history(period="1d")
        current_price = stock_info['Close'].iloc[-1]
        print(f"{name} ({ticker_symbol}) 현재 가격: {current_price} KRW/USD")
    except KeyError:
        print(f"{name} ({ticker_symbol})의 데이터를 가져올 수 없습니다.")
