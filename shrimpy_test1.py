import shrimpy
import plotly.graph_objects as go

public_key = '567126bdd87d83000c1b7d9ef16996cbfbee10db5860cd90ad96cee56261a98c '
secret_key = '7bd10b2b39339d8ae655c8a465b0ba34e5e8b3874e90f2bb1d5aa3271c516fff830ece1190cb5b702a0d4d9395e35e26624efd8795fa58ef5cb4b96629c1e7b4'

client = shrimpy.ShrimpyApiClient(public_key, secret_key)

candles = client.get_candles(
    'binance',  # exchange
    'COMP',      # base_trading_symbol
    'USDT',      # quote_trading_symbol
    '1m'       # interval
)

dates = []
open_data = []
high_data = []
low_data = []
close_data = []

for candle in candles:
    dates.append(candle['time'])
    open_data.append(candle['open'])
    high_data.append(candle['high'])
    low_data.append(candle['low'])
    close_data.append(candle['close'])



fig = go.Figure(data=[go.Candlestick(x=dates,
                       open=open_data, high=high_data,
                       low=low_data, close=close_data)])

fig.show()
