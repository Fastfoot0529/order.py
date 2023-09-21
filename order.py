import pyupbit

access = "8e3DU61NdWCwQfMZirxEjKRz6fD9LnwwxrXLWONd"          # 본인 값으로 변경
secret = "xka5VvVeEZ8knUgKC4AlXIfq3SuvBLuwDgs1GifQ"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

upbit.buy_market_order("KRW-BTC", 10000)
