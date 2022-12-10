import shrimpy
import socket
import time


public_key = '567126bdd87d83000c1b7d9ef16996cbfbee10db5860cd90ad96cee56261a98c '
secret_key = '7bd10b2b39339d8ae655c8a465b0ba34e5e8b3874e90f2bb1d5aa3271c516fff830ece1190cb5b702a0d4d9395e35e26624efd8795fa58ef5cb4b96629c1e7b4'

client = shrimpy.ShrimpyApiClient(public_key, secret_key)

candles = client.get_candles(
    'binance',  # exchange
    'COMP',      # base_trading_symbol
    'USDT',      # quote_trading_symbol
    '1m'       # interval
    )


UDP_IP = "127.0.0.1"
UDP_PORT = 3333

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
pause=2

for m in range(72000):

    candles = client.get_candles(
        'binance',  # exchange
        'COMP',      # base_trading_symbol
        'USDT',      # quote_trading_symbol
        '1m'       # interval
    )
    try:
        l = len(candles)
        price=(candles[l-1]['close']).strip()
        print(price)
        f2 = "%-5.0f" % ((float(price))*100)
        val1 = int(f2).to_bytes(8, byteorder='big')
        print ("val1",val1)
        sock.sendto(val1, (UDP_IP, UDP_PORT))
    except Exception as e:
        print("error:", e)




    time.sleep(pause)
